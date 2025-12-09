/**
 * AccentedLetterChips Component
 * Displays buttons to insert accented Italian letters into input fields
 */

const AccentedLetterChips = ({ inputRef, value, setValue, disabled }) => {
    const lowercaseLetters = ['à', 'è', 'é', 'ì', 'ò', 'ù'];
    const uppercaseLetters = ['À', 'È', 'É', 'Ì', 'Ò', 'Ù'];

    const handleInsert = (letter) => {
        if (disabled || !inputRef?.current) return;

        const input = inputRef.current;
        const start = input.selectionStart || 0;
        const end = input.selectionEnd || 0;
        const newValue = (value || '').substring(0, start) + letter + (value || '').substring(end);

        if (setValue) {
            setValue(newValue);
        } else {
            // Fallback: directly update the input value
            input.value = newValue;
            input.dispatchEvent(new Event('input', { bubbles: true }));
        }

        // Set cursor position after inserted letter
        setTimeout(() => {
            input.focus();
            input.setSelectionRange(start + 1, start + 1);
        }, 0);
    };

    return (
        <div className="space-y-2">
            <p className="text-xs text-gray-500 w-full mb-1">Click to insert accented letters:</p>
            {/* Lowercase letters row */}
            <div className="flex flex-wrap gap-2">
                {lowercaseLetters.map((letter) => (
                    <button
                        key={letter}
                        type="button"
                        onClick={() => handleInsert(letter)}
                        className="px-3 py-2 bg-gray-100 hover:bg-gray-200 border border-gray-300 rounded-lg text-lg font-medium text-gray-700 transition hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed"
                        disabled={disabled}
                    >
                        {letter}
                    </button>
                ))}
            </div>
            {/* Uppercase letters row */}
            <div className="flex flex-wrap gap-2">
                {uppercaseLetters.map((letter) => (
                    <button
                        key={letter}
                        type="button"
                        onClick={() => handleInsert(letter)}
                        className="px-3 py-2 bg-gray-100 hover:bg-gray-200 border border-gray-300 rounded-lg text-lg font-medium text-gray-700 transition hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed"
                        disabled={disabled}
                    >
                        {letter}
                    </button>
                ))}
            </div>
        </div>
    );
};

export default AccentedLetterChips;
