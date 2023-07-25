/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./**/templates/**/*.html'],
  theme: {
    extend: {
      colors: {
        primary: '#131118',
        secondary: '#2563eb',
        accent: '#db2777',
        neutral: '#f3f4f6',
        'base-100': '#FFFFFF',
        info: '#22d3ee',
        success: '#16a34a',
        warning: '#facc15',
        error: '#f43f5e',
      },
    },
  },
  plugins: [],
};
