/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './index.html',
    './index.tsx',
    './App.tsx',
    './src/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
    './pages/**/*.{js,ts,jsx,tsx}',
    './data/**/*.{js,ts}',
  ],
  theme: {
    extend: {
      fontFamily: {
        serif: ['"Playfair Display"', 'serif'],
        sans: ['"Inter"', 'sans-serif'],
      },
      colors: {
        tiffany: {
          DEFAULT: '#e63946',
          light: '#fca5a5',
          dark: '#C1121F',
          cream: '#f8fafc',
          ice: '#e2e8f0',
          obsidian: '#020617',
          obsidianLight: '#1e293b',
          gold: '#C5A880',
          rating: '#FBBF24',
        },
      },
    },
  },
  plugins: [],
};
