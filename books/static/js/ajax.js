const url = window.location.origin;
const heartIcon = document.querySelectorAll('.tuska');
const countFedback = document.querySelectorAll('#fcount');



heartIcon.forEach((el) =>{
    
    
    
    el.addEventListener('click',()=>{
        value = el.getAttribute("value");
        el.style = 'pointer-events:none;color:rgb(218, 187, 187);font-size:32px;'
        countFedback.forEach((count)=>{
            idka = count.getAttribute("value");
            if (idka===value){
                $.ajax({
                    type:"POST",
                    url:`${url}/fedback`,
                    dataType: "json",
                    data:{'id':value},
                    success: (data)=>{
                        if (data.status === "Error"){
                            alert("Siz Bu kitobga layk bosgansiz!");
                        }
                        else {
                            count.innerText = parseInt(count.innerText)+1;
                        }
                        
                    },
                    error: ()=>{
                        alert("Siz Bu kitobga layk bosgansiz!");
                    }
                })
                  
            } 
        })

       
        
    })
})