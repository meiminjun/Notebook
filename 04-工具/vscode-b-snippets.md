## mobile

```javascript
{
	// Example:
	// "Print to console": {
	// 	"scope": "javascript,typescript",
	// 	"prefix": "log",
	// 	"body": [
	// 		"console.log('$1');",
	// 		"$2"
	// 	],
	// 	"description": "Log output to console"
	// }
	"Print to Request": {
		"scope": "javascript,typescript,vue",
		"prefix": "req",
		"body": [
			"request({",
                "\tqs: {},",
				"\turl: $1",
            "})",
            ".then(response => {",
                "\t$0",
            "})",
            ".catch(err => {",
                "\tconsole.log(err);",
            "});"
		],
		"description": "print request"
	},
	"vuec": {
		"scope": "javascript,typescript,vue",
		"prefix": "vuec",
		"body": [
			"<template>",
				"\t<div>",
					"\t\t<Hd :config=\"headConfig\">",
						"\t\t\t<a class=\"btn\" style='background:transparent;color:inherit;font-size:0.32rem' @click=\"headConfig.rightButtonCallback()\">{{headConfig.rightButtonText}}</a>",
					"\t\t</Hd>",
					"\t\t<Loading :show=\"common.loading\"></Loading>",
				"\t</div>",
			"</template>",
			"<script>",
				"import { mapState } from 'vuex';",
				"import Hd from '../../components/PageHead.vue';",
				"import { nav } from '../../util/ald.js';",
				"import * as sdc from '../../util/sdc';",
				"import {  } from '../../api/urls.js';",
				"import Loading from '../../components/Loading.vue';",
				"import request from '../../components/aum-common/untils/request.js';",
				"export default {",
				"\tcomponents: {",
					"\t\tHd,",
					"\t\tLoading,",
				"\t},",
				"\tdata: function () {",
				"\t\treturn {",
					"\t\t\theadConfig: {",
						"\t\t\t\tleftButtonCallback: () => {",
							"$1",
						"\t\t\t\t},",
						"\t\t\t\trightButtonText: '关闭',",
						"\t\t\t\trightButtonCallback: () => {",
							"$2",
						"\t\t\t\t}",
					"\t\t\t}",
				"\t\t};",
				"\t},",
				"\tcomputed: {",
					"\t\t...mapState([",
						"\t\t\t'common'",
					"\t\t])",
				"\t},",
				"\tcreated: function () {$0},",
				"\tmounted: function () {$4},",
				"\tmethods: {$3}",
			"</script>",
		]
	},
	"headMixin": {
		"scope": "javascript,typescript,vue",
		"prefix": "headMixin",
		"body": [
			"const mixin = {",
				"\tdata: function () {",
					"\t\treturn {",
						"\t\t\theadConfig: {",
							"\t\t\t\ttitle: '标题',",
							"\t\t\t\tleftButtonVisible: true,",
							"\t\t\t\tbackgroundColor: '#f37937',",
							"\t\t\t\tcolor: '#ffffff',",
							"\t\t\t\tleftButtonIconTintColor: '#ffffff',",
							"\t\t\t\tleftButtonCallback: () => {},",
							"\t\t\t\trightButtonVisible: false,",
							"\t\t\t\trightButtonText: '关闭',",
							"\t\t\t\trightButtonTextColor: '#ffffff',",
							"\t\t\t\trightButtonCallback: () => {}",
						"\t\t\t}",
					"\t\t};",
				"\t}",
			"};",
		]
	}
}
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4MjU0NTAyMjFdfQ==
-->