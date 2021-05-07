// button add new semester, discipline or taskes
const bntAdd = document.getElementById("m-btn-add");
const divAdd = document.getElementById("m-div-add");

const dateInput = document.getElementById("id_delivery_at");
if(dateInput){
    dateInput.type = "date";
}

let bntAddActive = true; 

bntAdd.onclick = function () {
    if (!bntAddActive) {
        addAndRemove(bntAdd, "bi-plus-square-fill", "bi-x-square-fill");
        showDivAdd();
    } else {
        addAndRemove(bntAdd, "bi-x-square-fill", "bi-plus-square-fill");
        divAdd.style.display = "flex";
    }
    bntAddActive = !bntAddActive;
};

function addAndRemove(obj, add, remove) {
    if (remove) obj.classList.remove(remove);
    if (add) obj.classList.add(add);
}

function showDivAdd() {
    divAdd.style.setProperty('--animate-duration', '2s');
    addAndRemove(divAdd, "animate__animated");
    addAndRemove(divAdd, "animate__fadeInDown");
    divAdd.style.x = 1
    divAdd.style.y = 1
}

function closeDivAdd(){
    divAdd.style.display = "none";
    bntAddActive = !bntAddActive;
    addAndRemove(bntAdd, "bi-plus-square-fill", "bi-x-square-fill");
}


function showMCard(id, idbtn){
    if(document.getElementById(id).style.display == "none"){
        document.getElementById(id).style.display = "block";
        document.getElementById(idbtn).textContent = "Ocultar";
    }else{
        document.getElementById(id).style.display = "none";
        document.getElementById(idbtn).textContent = "Ver tarefas";
    }
}