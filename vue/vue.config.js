module.exports = {
  transpileDependencies: [
    'vuetify'
  ],
  devServer: {
    proxy: {
      "/data/": {
        target: "http://localhost:8000/",
      }
    }
  }
}