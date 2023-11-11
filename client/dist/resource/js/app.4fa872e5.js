(function(){"use strict";var e={6833:function(e,n,t){var a=t(9242),i=t(3396),l=t(7139),o=t(4870),s=t(2483);const r={class:"luminance"},u={class:"value"},c={class:"wrapper"},v={class:"util"};var d={__name:"App",setup(e){const n=(0,o.iH)(0),t=(0,o.iH)(!0),a=(async()=>{while(t.value){let t=0;try{const e=await fetch("/api/cds");t=(await e.json())?.value||NaN}catch(e){console.log(e)}n.value=t,await new Promise((e=>setTimeout(e,1e3)))}return!0})();return console.log(a),(e,t)=>((0,i.wg)(),(0,i.iD)(i.HY,null,[(0,i._)("header",null,[(0,i._)("div",r,[(0,i._)("div",u,(0,l.zw)(n.value),1)]),(0,i._)("div",c,[(0,i._)("div",v,[(0,i._)("button",{class:"btn btn-radius-solid",onClick:t[0]||(t[0]=(...e)=>console.log&&console.log(...e))},"ドアを開錠する")]),(0,i._)("nav",null,[(0,i.Wm)((0,o.SU)(s.rH),{to:"/irtable"},{default:(0,i.w5)((()=>[(0,i.Uk)("信号一覧")])),_:1})])])]),(0,i.Wm)((0,o.SU)(s.MA))],64))}},f=t(89);const p=(0,f.Z)(d,[["__scopeId","data-v-58866452"]]);var k=p;const _=e=>((0,i.dD)("data-v-37a5bbe1"),e=e(),(0,i.Cn)(),e),w={class:"wrap"},y=_((()=>(0,i._)("h1",null,"信号一覧",-1))),b={class:"operation-wrapper"},m=["onClick"],h=["onClick"],g=["onClick"],C={class:"memo"},x={class:"bold"},D={class:"signal"},O={key:1,class:"darkbox"},j={class:"inline"},H={class:"btns"},T={key:2,class:"darkbox"},U={class:"btns"};var E={__name:"IRTableView",setup(e){const n=[{text:"key",value:"key",sortable:!0},{text:"desc",value:"desc",sortable:!0},{text:"_",value:"operation"}],t=(0,o.iH)([]),s=(0,o.iH)([]),r=(0,o.iH)(!1),u=(0,o.iH)(!1),c=(0,o.iH)(!1),v=async()=>{r.value=!0;const e=await fetch("/api/ir");if(200!=e.status)return!1;const n=await e.json();return s.value=Object.keys(n).map((e=>({key:e,...n[e]}))),r.value=!1,!0},d=()=>{u.value=!1},f=()=>{c.value=!1},p=async e=>{const{key:n}=e;r.value=!0;const t=await fetch(`/api/ir/${n}`);if(200!=t.status)return alert("Communication failed."),!1;r.value=!1},k=(0,o.qj)({key:"",value:[],desc:""}),_=e=>{const{key:n,value:t,desc:a}=e;k.key=n,k.value=t,k.desc=a,u.value=!0},E=async()=>{const{key:e,desc:n}=k;if(!e)return alert("アイテム名は空欄にできません");r.value=!0;const t=await fetch(`/api/ir/${e}`,{method:"PUT",headers:{"Content-Type":"application/json"},body:JSON.stringify({desc:n})});if(200!=t.status)return alert("Communication failed."),!1;d(),await v()},z=(0,o.qj)({key:""}),q=e=>{z.key=e.key,c.value=!0},P=async(e=null,n=!1)=>{r.value=!0;let{key:t}=z;e&&(t=e);const a=await fetch(`/api/ir/${t}`,{method:"DELETE"});if(200!=a.status)return alert("Communication failed."),!1;n||(f(),await v())},S=async()=>{confirm("本当に削除しますか？")&&(r.value=!0,await Promise.all(t.value.map((e=>P(e.key,!0)))),f(),await v())};return v(),(e,o)=>{const I=(0,i.up)("EasyDataTable");return(0,i.wg)(),(0,i.iD)("div",w,[y,(0,i._)("a",{onClick:o[0]||(o[0]=e=>v())},"最新の情報に更新する"),(0,i.Wm)(I,{"show-index":"","items-selected":t.value,"onUpdate:itemsSelected":o[1]||(o[1]=e=>t.value=e),"buttons-pagination":"",headers:n,items:s.value,loading:r.value,alternating:""},{"item-operation":(0,i.w5)((e=>[(0,i._)("div",b,[(0,i._)("div",null,[(0,i._)("a",{onClick:n=>p(e)},"送出",8,m)]),(0,i._)("div",null,[(0,i._)("a",{onClick:n=>_(e)},"編集",8,h)]),(0,i._)("div",null,[(0,i._)("a",{onClick:n=>q(e)},"削除",8,g)])])])),expand:(0,i.w5)((e=>[(0,i._)("div",C,[(0,i._)("div",null,[(0,i._)("span",x,"value ("+(0,l.zw)(e.value.length)+"): ",1),(0,i._)("div",D,[((0,i.wg)(!0),(0,i.iD)(i.HY,null,(0,i.Ko)(e.value,((e,n)=>((0,i.wg)(),(0,i.iD)("span",{class:"signal_item",key:n},(0,l.zw)(e),1)))),128))])])])])),_:1},8,["items-selected","items","loading"]),t.value.length?((0,i.wg)(),(0,i.iD)("a",{key:0,onClick:o[2]||(o[2]=e=>S())},(0,l.zw)(t.value.length)+" 件のアイテムを削除",1)):(0,i.kq)("",!0),u.value?((0,i.wg)(),(0,i.iD)("div",O,[(0,i._)("h3",null,[(0,i.Uk)('Editing "'),(0,i._)("pre",j,(0,l.zw)(k.key),1),(0,i.Uk)('":')]),(0,i._)("div",null,[(0,i._)("div",null,[(0,i.Uk)("desc:"),(0,i.wy)((0,i._)("input",{type:"text","onUpdate:modelValue":o[3]||(o[3]=e=>k.desc=e)},null,512),[[a.nr,k.desc]])])]),(0,i._)("div",H,[(0,i._)("button",{onClick:o[4]||(o[4]=e=>E())},"Save"),(0,i._)("button",{onClick:o[5]||(o[5]=e=>d())},"Cancel")])])):(0,i.kq)("",!0),c.value?((0,i.wg)(),(0,i.iD)("div",T,[(0,i._)("h3",null,'Delete "'+(0,l.zw)(z.key)+'"?',1),(0,i._)("div",U,[(0,i._)("button",{onClick:o[6]||(o[6]=e=>P())},"Delete"),(0,i._)("button",{onClick:o[7]||(o[7]=e=>f())},"Cancel")])])):(0,i.kq)("",!0)])}}};const z=(0,f.Z)(E,[["__scopeId","data-v-37a5bbe1"]]);var q=z;const P=(0,s.p7)({history:(0,s.r5)(),routes:[{path:"/irtable",name:"irtable",component:q}]});var S=P,I=t(5893);const N=(0,a.ri)(k);N.component("EasyDataTable",I.Z),N.use(S),N.mount("#app")}},n={};function t(a){var i=n[a];if(void 0!==i)return i.exports;var l=n[a]={exports:{}};return e[a].call(l.exports,l,l.exports,t),l.exports}t.m=e,function(){var e=[];t.O=function(n,a,i,l){if(!a){var o=1/0;for(c=0;c<e.length;c++){a=e[c][0],i=e[c][1],l=e[c][2];for(var s=!0,r=0;r<a.length;r++)(!1&l||o>=l)&&Object.keys(t.O).every((function(e){return t.O[e](a[r])}))?a.splice(r--,1):(s=!1,l<o&&(o=l));if(s){e.splice(c--,1);var u=i();void 0!==u&&(n=u)}}return n}l=l||0;for(var c=e.length;c>0&&e[c-1][2]>l;c--)e[c]=e[c-1];e[c]=[a,i,l]}}(),function(){t.n=function(e){var n=e&&e.__esModule?function(){return e["default"]}:function(){return e};return t.d(n,{a:n}),n}}(),function(){t.d=function(e,n){for(var a in n)t.o(n,a)&&!t.o(e,a)&&Object.defineProperty(e,a,{enumerable:!0,get:n[a]})}}(),function(){t.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){t.o=function(e,n){return Object.prototype.hasOwnProperty.call(e,n)}}(),function(){var e={143:0};t.O.j=function(n){return 0===e[n]};var n=function(n,a){var i,l,o=a[0],s=a[1],r=a[2],u=0;if(o.some((function(n){return 0!==e[n]}))){for(i in s)t.o(s,i)&&(t.m[i]=s[i]);if(r)var c=r(t)}for(n&&n(a);u<o.length;u++)l=o[u],t.o(e,l)&&e[l]&&e[l][0](),e[l]=0;return t.O(c)},a=self["webpackChunkclient"]=self["webpackChunkclient"]||[];a.forEach(n.bind(null,0)),a.push=n.bind(null,a.push.bind(a))}();var a=t.O(void 0,[998],(function(){return t(6833)}));a=t.O(a)})();
//# sourceMappingURL=app.4fa872e5.js.map