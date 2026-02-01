import { defineConfig } from 'vite'
import { resolve } from 'path'

export default defineConfig({
  base: './',
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        dashboard: resolve(__dirname, 'dashboard.html'),
        login: resolve(__dirname, 'login.html'),
        resume: resolve(__dirname, 'resume.html'),
        analyze: resolve(__dirname, 'analyze.html'),
        features: resolve(__dirname, 'features.html')
      }
    }
  }
})
