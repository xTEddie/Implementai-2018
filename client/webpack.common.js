const HtmlWebPackPlugin = require("html-webpack-plugin");
module.exports = {
  entry: {
    app: ['@babel/polyfill', './src/index.js']
  },
  plugins: [
    new HtmlWebPackPlugin({
      template: "./dist/base.html",
      filename: "./index.html"
    })
  ],
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      },
      {
        test: /\.html$/,
        use: [
          {
            loader: "html-loader"
          }
        ]
      },
      {
        test: /\.s?css$/,
        loaders: [
          {
            loader: 'style-loader' // creates style nodes from JS strings
          },
          {
            loader: 'css-loader' // translates CSS into CommonJS
          },
          {
            loader: 'sass-loader' // compiles Sass to CSS
          }
        ]
      },
      {
        test: /\.(pdf|jpe?g|png|gif|svg|eot|ttf|woff|woff2)$/i,
        use: [{
          loader: "image-webpack-loader",
          options: {
            bypassOnDebug: true,
            optipng: {
              optimizationLevel: 7,
            },
            gifsicle: {
              interlaced: false
            }
          }
        }, {
          loader: 'file-loader?hash=sha512&digest=hex&name=[hash].[ext]'
        }]
      }
    ]
  }
};
