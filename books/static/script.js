const srch = document.querySelector('#searchTxt');
const btn = document.querySelector('#btnnn');
srch.addEventListener('input',()=>{
    const val = srch.value
    if (val.length > 0) {
      btn.classList.remove("disabled")
    }
    else {
        btn.classList.add("disabled")

    }

})
const mes = document.querySelector('#knl');
const myTimeout = setTimeout(()=>{
    mes.style.display = 'none'
}, 3000);






