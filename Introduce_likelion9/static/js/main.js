
 (()=> {
    const stepElems = document.querySelectorAll('.step');
    const graphicElems = document.querySelectorAll('.graphic-item');
    let currentItem; 
    for (let i = 0 ; i < stepElems.length; i++){
        stepElems[i].dataset.index = i;
        graphicElems[i].dataset.index = i;
    }

    
    window.addEventListener('scroll', () => {
        let step;
        let boundingRect;

        for (let i = 0 ; i < stepElems.length; i++){
            step = stepElems[i];
            boundingRect = step.getBoundingClientRect();
           //  console.log(boundingRect);
           //  console.log(boundingRect.top);

           if ( boundingRect.top > window.innerHeight * 0.1 &&
                boundingRect.top < window.innerHeight * 0.8) {
               console.log(step.dataset.index);

               if (currentItem){
                   currentItem.classList.remove('visible');
               }
               currentItem = graphicElems[step.dataset.index]
               currentItem.classList.add('visible');
           }
        }
    })
}) ();