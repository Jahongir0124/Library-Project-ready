const btn_o = document.querySelector('#btn-o');
const btn_c = document.querySelector('#btn-c');
const div = document.querySelector('.c-active');
const markup = document.querySelector('#btn');
const text = document.querySelector('#text_c');
div.style.display = 'none';

btn_c.style.display='none';


btn_o.addEventListener('click',()=>{
    btn_c.style.display = 'block';
    btn_o.style.display = 'none';
    div.style.display = 'block'

})
btn_c.addEventListener('click',()=>{
    btn_o.style.display = 'block';
    btn_c.style.display = 'none';
    div.style.display = 'none';
    
})

text.addEventListener('input',()=>{
	const val = text.value;
	if (val.length > 0) {
		 markup.classList.remove("disabled")

	}
	 else {
        markup.classList.add("disabled")

    }
})