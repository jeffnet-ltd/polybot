# OAuth Authentication Debugging Guide

**Issue:** Users are redirected back to landing page after Google OAuth login instead of reaching the lesson screen.

**Status:** Enhanced debugging has been added to help diagnose the issue.

---

## Quick Debugging Steps

### Step 1: Open Browser DevTools

1. Open PolyBot in your browser
2. Open **Developer Tools** (F12 or Right-click → Inspect)
3. Go to the **Console** tab
4. Clear any existing logs

### Step 2: Attempt Google OAuth Login

1. Click "Continue with Google"
2. Complete Google authentication
3. **DO NOT** close DevTools

### Step 3: Check Console Logs

Look for logs starting with `[OAuth]` and `[LoadProfile]`.

**Expected Sequence:**
```
[OAuth] Processing OAuth callback with userId: abc123def456
[OAuth] isNewUser: false hasError: false
[OAuth] Email: user@example.com Name: John Doe
[OAuth] Returning user - loading profile
[LoadProfile] Loading profile for email: user@example.com
[LoadProfile] Profile loaded successfully: {user_id: "...", email: "...", ...}
[LoadProfile] Setting view to main
```

---

## Possible Scenarios and Solutions

### Scenario 1: OAuth logs never appear

**What it means:** The OAuth effect isn't running at all

**Possible causes:**
- URL params aren't being set by backend
- useEffect dependency is causing issues
- Frontend isn't receiving the redirect

**Debug steps:**
1. Check browser address bar after OAuth - do you see `?user_id=...&email=...`?
2. If YES → proceed to Scenario 2
3. If NO → Check backend OAuth endpoint logs:
   ```bash
   docker logs polybot-backend | grep -i oauth
   ```

### Scenario 2: OAuth logs appear, but view doesn't change

**What it means:** OAuth effect ran, but `setView('main')` wasn't called

**Log sequence would be:**
```
[OAuth] Processing OAuth callback...
[OAuth] isNewUser: false
[OAuth] Returning user - loading profile
(then nothing, or LoadProfile logs don't appear)
```

**Possible causes:**
- `getUserProfile` API call is failing silently
- Network issue
- Backend `/user/profile` endpoint not responding

**Debug steps:**
1. Check Network tab in DevTools
2. Look for a request to `/user/profile?email=...`
3. Check the response status code:
   - **200** = Success but still having issues
   - **404** = User not found in database
   - **500** = Backend error
4. Check backend logs:
   ```bash
   docker logs polybot-backend | tail -50
   ```

### Scenario 3: LoadProfile logs appear but view still doesn't change

**What it means:** Profile loaded but `setView('main')` may be happening too late

**Log sequence:**
```
[OAuth] Processing OAuth callback...
[LoadProfile] Loading profile for email: ...
[LoadProfile] Profile loaded successfully: {...}
[LoadProfile] Setting view to main
(but screen still shows landing page)
```

**Possible causes:**
- Race condition where view is being reset after it's set
- Another effect is running and resetting the view
- State update isn't causing a re-render

**Debug steps:**
1. Add a watchpoint for `view` state (advanced browser debugging)
2. Check if there are multiple renders happening
3. Look for any other logs that might indicate what's happening after the view change

### Scenario 4: LoadProfile fails with error

**Log sequence:**
```
[OAuth] Returning user - loading profile
[LoadProfile] Loading profile for email: user@example.com
[LoadProfile] Failed to load profile: Error: 404 User not found
```

**Possible causes:**
- User database record doesn't exist
- Email mismatch between OAuth and backend
- Backend database connection issue

**Debug steps:**
1. Check MongoDB directly:
   ```bash
   docker exec polybot-mongodb mongosh
   > use polybot_database
   > db.users.find({email: "user@example.com"})
   ```
2. Verify user was created by OAuth callback
3. Check if OAuth is creating users correctly (backend should auto-create on first login)

---

## Network Debugging

### Check API Calls

1. Open DevTools → **Network** tab
2. Go through OAuth login process again
3. Look for these requests:
   - `POST /api/google/login` - Initial OAuth request
   - `GET /user/profile?email=...` - Profile loading
   - Any error responses (4xx, 5xx codes)

### Check Backend Logs

```bash
# Watch backend logs in real-time
docker logs -f polybot-backend

# Search for specific issue
docker logs polybot-backend | grep -A 5 -B 5 "user@example.com"
```

### Check Frontend Logs

1. DevTools Console for `[OAuth]` and `[LoadProfile]` messages
2. Check for any red errors or warnings
3. Look for network errors (CORS, connection refused, etc.)

---

## Flow Diagram

```
User clicks "Continue with Google"
    ↓
Frontend redirects to backend OAuth endpoint
    ↓
/api/google/login → Google OAuth server
    ↓
Backend receives OAuth token
    ↓
Backend creates/fetches user in MongoDB
    ↓
Backend redirects to /?user_id=...&email=...&new_user=false
    ↓
Frontend useEffect runs
    ├─ Checks if already processed (useRef guard)
    ├─ Extracts userId from URL
    ├─ Checks if new or returning user
    └─ If returning: calls handleLoadProfile(email)
    ↓
handleLoadProfile calls getUserProfile(email)
    ↓
API call: GET /user/profile?email=user@example.com
    ↓
Backend returns user profile from MongoDB
    ↓
Frontend updates userProfile state
    ↓
Frontend calls setView('main')
    ↓
Component re-renders
    ↓
User sees lesson screen ✅
```

---

## Common Issues and Fixes

### Issue: "Login Failed: OAuth State Failed"

**Cause:** OAuth state validation failed

**Solution:**
1. Clear browser cookies for localhost
2. Try logging in again
3. Check backend logs for OAuth errors:
   ```bash
   docker logs polybot-backend | grep -i "oauth\|google"
   ```

### Issue: "User not found" but OAuth succeeded

**Cause:** User was created but email doesn't match

**Solution:**
1. Check what email the user signed up with
2. Verify in MongoDB that user record has correct email
3. May need to manually fix email in database or recreate user

### Issue: Long delay before redirect

**Cause:** Network latency or slow profile loading

**Solution:**
1. Check backend performance
2. Look at API response times in Network tab
3. Check MongoDB query performance
4. May need to add indexes to email field:
   ```bash
   docker exec polybot-mongodb mongosh
   > use polybot_database
   > db.users.createIndex({email: 1})
   ```

---

## Advanced Debugging

### React DevTools

If you have React DevTools browser extension:
1. Open it alongside Console
2. Navigate to the App component
3. Watch the `view` state change in real-time
4. See when renders are triggered

### Adding More Logging

If you need more detailed debugging, edit `frontend/src/App.jsx` and add logs in these places:

```javascript
// In handleLoadProfile, before setUserProfile:
console.log('[LoadProfile] Response data:', {
    user_id: responseData.user_id,
    email: responseData.email,
    native_language: responseData.native_language,
    target_language: responseData.target_language,
});

// In OAuth effect, check state before setView:
console.log('[OAuth] About to set view to:', isNewUser ? 'language_setup' : 'main');
console.log('[OAuth] Current view state:', view);
```

### Check Component Props

In MainScreen component, add logging to see if it's receiving props:
```javascript
console.log('[MainScreen] Mounted with userProfile:', userProfile);
```

---

## Files to Check

| File | Purpose | Check |
|------|---------|-------|
| `frontend/src/App.jsx` | Main component with OAuth logic | Lines 1981-2047 |
| `frontend/src/services/userService.js` | API calls | `getUserProfile` function |
| `backend/server.py` | OAuth endpoint | Lines 1454-1487 |
| `backend/server.py` | Profile endpoint | Lines 1509-1515 |

---

## Reporting Issues

When reporting this issue, please include:

1. **Console logs:** Screenshot or copy of `[OAuth]` and `[LoadProfile]` messages
2. **Network tab:** Screenshots showing API requests and responses
3. **Browser/OS:** What browser and OS you're using
4. **Steps to reproduce:** Exactly what you did before the issue occurred
5. **Expected vs actual:** What you expected to happen vs what actually happened

---

## Next Steps

1. **Rebuild frontend:** `docker-compose down && docker-compose up -d --build frontend`
2. **Test OAuth login:** Follow Quick Debugging Steps above
3. **Check console logs:** Look for `[OAuth]` and `[LoadProfile]` messages
4. **Identify failure point:** Use Possible Scenarios section to locate where it fails
5. **Report findings:** Include console output and network tab screenshots

The detailed logging will help us pinpoint exactly where the authentication flow is breaking down.

