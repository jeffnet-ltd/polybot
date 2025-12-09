/**
 * FormFillExercise Component
 *
 * A form-filling exercise for practicing structured responses.
 * Features field validation and custom validation rules for language learning.
 */

import React, { useState } from 'react';

const FormFillExercise = ({ prompt, formFields, targetLang, onAnswer, explanation }) => {
    const [formData, setFormData] = useState({});
    const [hasSubmitted, setHasSubmitted] = useState(false);
    const [validationErrors, setValidationErrors] = useState({});

    const handleFieldChange = (fieldLabel, value) => {
        setFormData(prev => ({ ...prev, [fieldLabel]: value }));
        // Clear validation error for this field
        if (validationErrors[fieldLabel]) {
            setValidationErrors(prev => {
                const newErrors = { ...prev };
                delete newErrors[fieldLabel];
                return newErrors;
            });
        }
    };

    const validateField = (field, value) => {
        if (field.required && !value) {
            return `${field.label} is required`;
        }
        if (field.validation === "name" && value) {
            const hasName = value.toLowerCase().includes("mi chiamo") || value.toLowerCase().includes("sono ") || value.toLowerCase().includes("io sono");
            if (!hasName) return "Use 'Mi chiamo [name]' or 'Sono [name]' format";
        }
        if (field.validation === "origin" && value) {
            const hasOrigin = value.toLowerCase().includes("sono di") || value.toLowerCase().includes("di italia") || value.toLowerCase().includes("di francia");
            if (!hasOrigin) return "Use 'Sono di [country]' format";
        }
        return null;
    };

    const handleSubmit = () => {
        const errors = {};
        let allValid = true;

        formFields.forEach(field => {
            const value = formData[field.label] || '';
            const error = validateField(field, value);
            if (error) {
                errors[field.label] = error;
                allValid = false;
            }
        });

        setValidationErrors(errors);
        setHasSubmitted(true);

        if (allValid) {
            // Check if all required fields are filled
            const allRequiredFilled = formFields.every(field => !field.required || formData[field.label]);
            onAnswer(allRequiredFilled ? 'correct' : 'almost', formData, explanation || "Perfect! All fields filled correctly.");
        } else {
            onAnswer('incorrect', formData, "Please fill all required fields correctly.");
        }
    };

    return (
        <div className="space-y-6">
            <h3 className="text-xl font-semibold text-gray-800 text-center">{prompt}</h3>
            <div className="bg-white border-2 border-gray-300 rounded-2xl p-6 space-y-4">
                {formFields.map((field, idx) => (
                    <div key={idx} className="space-y-2">
                        <label className="block text-sm font-medium text-gray-700">
                            {field.label}
                            {field.required && <span className="text-red-500 ml-1">*</span>}
                        </label>
                        {field.type === "text" ? (
                            <input
                                type="text"
                                value={formData[field.label] || ''}
                                onChange={(e) => handleFieldChange(field.label, e.target.value)}
                                placeholder={field.hint || ""}
                                disabled={hasSubmitted}
                                className={`w-full p-3 border rounded-xl focus:ring-2 focus:ring-blue-500 ${validationErrors[field.label] ? 'border-red-300' : 'border-gray-300'
                                    }`}
                            />
                        ) : field.type === "select" ? (
                            <select
                                value={formData[field.label] || ''}
                                onChange={(e) => handleFieldChange(field.label, e.target.value)}
                                disabled={hasSubmitted}
                                className={`w-full p-3 border rounded-xl focus:ring-2 focus:ring-blue-500 ${validationErrors[field.label] ? 'border-red-300' : 'border-gray-300'
                                    }`}
                            >
                                <option value="">Select...</option>
                                {field.options.map((opt, optIdx) => (
                                    <option key={optIdx} value={opt}>{opt}</option>
                                ))}
                            </select>
                        ) : null}
                        {field.hint && !validationErrors[field.label] && (
                            <p className="text-xs text-gray-500">{field.hint}</p>
                        )}
                        {validationErrors[field.label] && (
                            <p className="text-xs text-red-600">{validationErrors[field.label]}</p>
                        )}
                    </div>
                ))}
            </div>
            <button
                onClick={handleSubmit}
                disabled={hasSubmitted}
                className="w-full py-4 rounded-2xl font-bold text-white bg-gradient-to-r from-green-600 to-blue-600 hover:from-green-700 hover:to-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed shadow-md transition transform hover:scale-[1.02]"
            >
                {hasSubmitted ? "Submitted" : "Submit Form"}
            </button>
        </div>
    );
};

FormFillExercise.displayName = 'FormFillExercise';

export default FormFillExercise;
