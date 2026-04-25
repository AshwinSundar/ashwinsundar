/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./content/**/*.md",
    "./data/**/*.json",
  ],
  safelist: [
    // dynamic music card colors from data/music.json
    "bg-red-500", "bg-pink-500", "bg-yellow-500",
    "bg-green-500", "bg-green-200", "bg-blue-200", "bg-orange-500",
  ],
  theme: {
    fontFamily: {
      sans: ["EversonMono", "monospace"],
    },
    extend: {
      colors: {
        paper: "#fff1e5",
      },
    },
  },
  plugins: [],
}
