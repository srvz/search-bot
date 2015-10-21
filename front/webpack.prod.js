var webpack = require("webpack");
var bowerWebpackPlugin = require('bower-webpack-plugin');

module.exports = {
	entry : {
		main: './src/js/main.js'
	},
	output: {
		path: '../static/dist',
		filename: '[name].min.js'
	},
	module: {
		loaders: [
			{test: /\.js$/, loader: 'babel-loader', exclude: /(node_modules|bower_components)/},
			{test: /\.css$/, loader: 'style-loader!css-loader!autoprefixer-loader' },
			{test: /\.html$/, loader: 'html-loader'},
			{test: /\.(png|jpg|gif)$/, loader: 'url-loader?limit=819200&name=../assets/[hash].[ext]'},
			{test: /\.jade/, loader: "jade-loader" },
			{test: /\.less$/, loader: 'style-loader!css-loader!autoprefixer-loader!less-loader' },
			{test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: "url-loader?limit=10000&minetype=application/font-woff" },
			{test: /\.(ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: "file-loader?name=../assets/[hash].[ext]" }
		]
	},
	plugins: [
		new bowerWebpackPlugin(),
		new webpack.optimize.UglifyJsPlugin({compress: {warnings: false}})
	]
};