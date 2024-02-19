/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["content/**/*.md", "layouts/**/*.html"],
  theme: {
    fontFamily: {
      sans: ["EversonMono", "monospace"],
    },
    extend: {
      colors: {
        paper: "#fff1e5", // background color
      }
    },
  },
  plugins: [],
}

