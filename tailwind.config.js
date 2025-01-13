/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './templates/**/*.html',
        './edutech/**/*.html',   
        './schools/**/*.html', 
        './home/**/*.html',   
        './tenant_manager/**/*.html', 
        './static/**/*.js',
        "./static/src/**/*.{html,js}"     
      ],
    theme: {
      extend: {},
    },
    plugins: [require('@tailwindcss/forms'),],
  }