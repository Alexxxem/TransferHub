document.addEventListener("DOMContentLoaded", function () {
    // При загрузке страницы скрываем все таблицы, кроме "player-table"
    var tables = document.querySelectorAll('.profile-table');
    tables.forEach(function (table) {
        table.style.display = 'none';
    });

    // Отображаем "player-table"
    var playerTable = document.getElementById('player-table');
    playerTable.style.display = 'table';

    // Отображаем кнопку "Add" и привязываем ее к форме "player-form"
    var addButton = document.getElementById('add-button');
    addButton.style.display = 'block';
    addButton.onclick = function () {
        showForm('player-form');
    };
});

function showTable(tableName, formId) {
    // Скрыть все таблицы
    var tables = document.querySelectorAll('.profile-table');
    tables.forEach(function (table) {
        table.style.display = 'none';
    });

    // Отобразить выбранную таблицу
    var selectedTable = document.getElementById(tableName);
    selectedTable.style.display = 'table';

    // Отобразить кнопку "Add" и привязать ее к соответствующей форме
    var addButton = document.getElementById('add-button');
    addButton.style.display = 'block';
    addButton.onclick = function () {
        showForm(formId);
    };
}

function showForm(formId) {
    openModal();

    // Скрыть все формы
    var forms = document.querySelectorAll('.modal-content form');
    forms.forEach(function (form) {
        form.style.display = 'none';
    });

    // Отобразить выбранную форму
    var selectedForm = document.getElementById(formId);
    selectedForm.style.display = 'block';
}

function openModal() {
    var modal = document.getElementById('modal');
    var modalContent = document.querySelector('.modal-content');
    modal.style.display = 'block';
    modalContent.style.display = 'block';
}

function closeModal() {
    var modal = document.getElementById('modal');
    var modalContent = document.querySelector('.modal-content');
    modal.style.display = 'none';
    modalContent.style.display = 'none';
}

