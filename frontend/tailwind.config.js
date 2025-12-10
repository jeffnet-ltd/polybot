/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // Brand Colors - Lime Green Accent
        'brand-lime': {
          50: '#f7fee7',
          100: '#ecfccf',
          200: '#d9f99d',
          300: '#bef264',
          400: '#a3e635',
          500: '#84cc16',
          600: '#65a30d',
          700: '#4d7c0f',
          800: '#3f6212',
          900: '#365314',
        },
        // Brand Colors - Indigo Secondary
        'brand-indigo': {
          50: '#eef2ff',
          100: '#e0e7ff',
          600: '#4f46e5',
          700: '#4338ca',
        },
        // Brand Colors - Amber Accent
        'brand-amber': {
          500: '#f59e0b',
          600: '#d97706',
        },
      },
      animation: {
        // Entrance animations
        'slide-up': 'slideUpFade 0.4s ease-out',
        'fade-in-stagger': 'fadeIn 0.4s ease-out',

        // Highlight animations
        'pulse-glow': 'pulseGlow 2s ease-in-out infinite',

        // Fill animations
        'fill-bar': 'fillBar 1s ease-out forwards',

        // Action animations
        'bounce-scale': 'bounceScale 0.5s ease-in-out',
        'slide-right': 'slideRight 0.3s ease-out',
      },
      keyframes: {
        slideUpFade: {
          '0%': {
            opacity: '0',
            transform: 'translateY(20px)',
          },
          '100%': {
            opacity: '1',
            transform: 'translateY(0)',
          },
        },
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        pulseGlow: {
          '0%, 100%': {
            'box-shadow': '0 0 20px rgba(132, 204, 22, 0.4)',
          },
          '50%': {
            'box-shadow': '0 0 30px rgba(132, 204, 22, 0.8)',
          },
        },
        fillBar: {
          '0%': { width: '0%' },
          '100%': { width: '100%' },
        },
        bounceScale: {
          '0%, 100%': { transform: 'scale(1)' },
          '50%': { transform: 'scale(1.05)' },
        },
        slideRight: {
          '0%': { transform: 'translateX(0)' },
          '100%': { transform: 'translateX(4px)' },
        },
      },
      // Extended shadows for elevation levels
      boxShadow: {
        'elevation-1': '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
        'elevation-2': '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
        'elevation-3': '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
        'elevation-4': '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)',
        'glow-lime': '0 0 20px rgba(132, 204, 22, 0.4)',
        'glow-lime-strong': '0 0 30px rgba(132, 204, 22, 0.8)',
      },
      // Extended transitions for smooth effects
      transitionDuration: {
        'smooth': '300ms',
        'smooth-fast': '150ms',
        'smooth-slow': '500ms',
      },
    },
  },
  plugins: [],
};
