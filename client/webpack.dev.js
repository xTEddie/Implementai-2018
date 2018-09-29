const webpack = require('webpack');
const merge = require('webpack-merge');
const common = require('./webpack.common.js');

let API_HOST = 'localhost:8000';

module.exports = merge(common, {
  mode: 'development',
  plugins: [
    new webpack.DefinePlugin({
      'process.env': {
        'NODE_ENV': JSON.stringify(process.env.NODE_ENV),
        'API_ROOT': JSON.stringify(`http://${API_HOST}`)
      }
    })
  ]
});
