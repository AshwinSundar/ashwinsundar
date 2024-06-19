/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../../**/*.html", "../../**/*.md"],
  theme: {
    fontFamily: {
      sans: ["EversonMono", "monospace"],
    },
    extend: {
      colors: {
        paper: "#fff1e5", // background color
      },

    },
  },
  plugins: [],
}

