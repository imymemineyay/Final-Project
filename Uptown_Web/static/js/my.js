var morphTimeline = new TimelineMax({
    repeat:-1,
    repeatDelay:2
  });
  
  morphTimeline
    .timeScale(1.5)
    .to($('#megaphone'),2,{morphSVG:{shape:"#links"}, fill:"none",opacity:1})
    .to($('#megaphone'),2,{morphSVG:{shape:"#computer"}, fill:"none"},"+=2")
    .to($('#megaphone'),2,{morphSVG:{shape:"#light"}, fill:"none"},"+=2")
    .to($('#megaphone'),2,{morphSVG:{shape:"#megaphone"}, fill:"none"},"+=2")
  ;
  
  /*TweenMax.to($('#megaphone'),3,{stroke:"hsl(+=360,+=0%,+=0%)",repeat:-1,yoyo:true});*/
  
  /*TweenMax.to($('#megaphone'),3,{stroke:"hsl(+=0,+=0%,-=50%)",repeat:-1,yoyo:true,repeatDelay:0});*/