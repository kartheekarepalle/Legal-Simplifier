import { defineConfig } from "vite"
import react from "@vitejs/plugin-react"

export default defineConfig({
  base: "./",        // ensures correct paths for static build
  plugins: [react()] // enables React plugin
})
