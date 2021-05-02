// button add new semester, discipline or taskes
const bntAdd = document.getElementById("m-btn-add");
const divAdd = document.getElementById("m-div-add");

const dateInput = document.getElementById("id_delivery_at");
dateInput.type = "date";

divAdd.style.display = "none";

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


//////////////////////////////////////

function allowDrop(ev) {
    ev.preventDefault();
}

function dragStart(ev) {
    ev.dataTransfer.setData("text/plain", ev.target.id);
}

function dropIt(ev) {
    ev.preventDefault();
    let sourceId = ev.dataTransfer.getData("text/plain");
    let sourceIdEl = document.getElementById(sourceId);
    let sourceIdParentEl = sourceIdEl.parentElement;
    let targetEl = document.getElementById(ev.target.id)
    let targetParentEl = targetEl.parentElement;

    if (targetParentEl.id !== sourceIdParentEl.id) {
        if (targetEl.className === sourceIdEl.className) {
            targetParentEl.appendChild(sourceIdEl);
        } else {
            targetEl.appendChild(sourceIdEl);
        }

    } else {
        let holder = targetEl;
        let holderText = holder.textContent;
        targetEl.textContent = sourceIdEl.textContent;
        sourceIdEl.textContent = holderText;
        holderText = '';
    }
}