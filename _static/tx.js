window.onload= function(){
  const s = document.createElement('script');
  s.setAttribute("src","https://cdn.jsdelivr.net/npm/@transifex/native/dist/browser.native.min.js");
  s.setAttribute("type","text/javascript");
  s.onload=function(){
  const tx = Transifex.tx;
  const t = Transifex.t;
  tx.init({
    token: '1/5c5efef5446b45f57b080697f32e5a6903d0503e',
  });
  }
document.body.appendChild(s);
}
