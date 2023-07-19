const path = require('path');

module.exports = {
  entry: {
    products: path.resolve(__dirname, './static/js/products.js'),
  },
  watch: true,
  devtool: false,
  output: {
    path: path.resolve(__dirname, './static/js/dist'),
  },
  module: {
    rules: [
      {
        test: /\.css$/i,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
};
