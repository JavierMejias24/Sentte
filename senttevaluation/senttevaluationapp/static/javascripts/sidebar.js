$(document).ready(function(){
    let sidebar = document.querySelector(".sidebar");
    let sidebarBtn = document.querySelector(".bx-menu");
    sidebarBtn.addEventListener("click", ()=>{
        sidebar.classList.toggle("close");
    });
})