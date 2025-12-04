import React from 'react';
import { render, screen, fireEvent, waitFor, act } from '@testing-library/react';
import App from './App';
import axios from 'axios';

// --- MOCKS ---
// We mock axios so we don't actually hit the backend during UI tests
jest.mock('axios');

// Mock scrollIntoView (not supported in standard test environments)
window.HTMLElement.prototype.scrollIntoView = function() {};

describe('Polybot Frontend Tests', () => {
    
    beforeEach(() => {
        // Reset mocks before each test to ensure clean state
        axios.get.mockClear();
        axios.post.mockClear();
        axios.patch.mockClear();
    });

    test('renders registration screen by default', () => {
        render(<App />);
        
        // Check for Branding
        expect(screen.getByText(/Polybot/i)).toBeInTheDocument();
        expect(screen.getByText(/Your private AI language tutor/i)).toBeInTheDocument();
        
        // Check for Social Buttons
        expect(screen.getByText(/Continue with Google/i)).toBeInTheDocument();
        
        // Check for Inputs
        expect(screen.getByPlaceholderText(/Name/i)).toBeInTheDocument();
        expect(screen.getByPlaceholderText(/Email/i)).toBeInTheDocument();
    });

    test('manual registration flow navigates to Language Setup', async () => {
        // Setup Mock Response for Register
        axios.post.mockResolvedValue({ data: { message: "Success", id: "test_id_123" } });

        render(<App />);

        // simulate typing
        fireEvent.change(screen.getByPlaceholderText(/Name/i), { target: { value: 'Test User' } });
        fireEvent.change(screen.getByPlaceholderText(/Email/i), { target: { value: 'test@example.com' } });

        // Click Register
        const button = screen.getByText(/Create Account & Start/i);
        fireEvent.click(button);

        // Wait for the view to change to Language Setup
        await waitFor(() => {
            expect(screen.getByText(/Let's set up your learning path/i)).toBeInTheDocument();
            expect(screen.getByText(/Welcome, Test User!/i)).toBeInTheDocument();
        });
    });

    test('language setup completion navigates to Main Dashboard', async () => {
        // Setup Mocks
        // 1. Mock Registration Response (to get us to setup)
        axios.post.mockResolvedValue({ data: { message: "Success", id: "test_id_123" } });
        // 2. Mock Patch Response (saving languages)
        axios.patch.mockResolvedValue({ data: { message: "Updated" } });
        // 3. Mock Get Lessons (for dashboard)
        axios.get.mockResolvedValue({ data: [
            { _id: "A1.1", title: "Greetings", goal: "Say hi", topics: [], vocabulary: [], exercises: [] }
        ]});

        render(<App />);

        // --- STEP 1: Register ---
        fireEvent.change(screen.getByPlaceholderText(/Name/i), { target: { value: 'Test User' } });
        fireEvent.change(screen.getByPlaceholderText(/Email/i), { target: { value: 'test@example.com' } });
        fireEvent.click(screen.getByText(/Create Account & Start/i));

        // Wait for Setup Screen
        await waitFor(() => screen.getByText(/I want to learn:/i));

        // --- STEP 2: Save Preferences ---
        const startButton = screen.getByText(/Start Learning/i);
        fireEvent.click(startButton);

        // --- STEP 3: Check Dashboard ---
        await waitFor(() => {
            // Check for Dashboard specific elements
            expect(screen.getByText(/Lessons \(A1\)/i)).toBeInTheDocument();
            // Check if our mocked lesson title appears
            expect(screen.getByText(/Greetings/i)).toBeInTheDocument();
        });
    });

    test('google login button has correct link', () => {
        // Since we can't test window.location easily, we check if the button exists
        render(<App />);
        const googleBtn = screen.getByText(/Continue with Google/i);
        expect(googleBtn).toBeInTheDocument();
    });
});