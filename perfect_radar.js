csvUrl = 'https://raw.githubusercontent.com/johnnychao91/pkg/main/data/cp_list/bulbasaur_cp.csv';
const optionsCsvUrl = 'https://raw.githubusercontent.com/johnnychao91/pkg/main/data/pk_names.csv';

async function fetchOptions() {
    try {
        const response = await fetch(optionsCsvUrl);
        const text = await response.text();
        return parseCSV(text);
    } catch (error) {
        console.error('Error fetching options CSV:', error);
    }
}

function populateDropdown(options) {
    const dropdown = document.getElementById('pkOptions');
    dropdown.innerHTML = ''; // 清空之前的選項

    options.forEach(option => {
        const optionElement = document.createElement('option');
        optionElement.value = option[0];
        optionElement.textContent = option[2] + " " + option[1];
        dropdown.appendChild(optionElement);
    });
}

async function initDropdown() {
    const optionsData = await fetchOptions();
    optionsData.shift(); // 删除标题行
    populateDropdown(optionsData);
}

document.addEventListener('DOMContentLoaded', initDropdown);



const selectPokemon = document.getElementById("pkOptions");

selectPokemon.addEventListener("change", function() {
    const pokemonID = selectPokemon.value;
    csvUrl = 'https://raw.githubusercontent.com/johnnychao91/pkg/main/data/cp_list/' + pokemonID + '_cp.csv';

});

async function fetchData() {
    try {
        const response = await fetch(csvUrl);
        const text = await response.text();
        console.log(text);  // 在控制台中显示CSV文件的内容
        return text;
    } catch (error) {
        console.error('Error fetching CSV:', error);
    }
}
function parseCSV(text) {
    // 處理Windows 和 Unix/Linux 系统的換行符
    const rows = text.split(/\r?\n/).filter(row => row.trim() !== '');
    const data = rows.map(row => row.split(','));
    console.log(data);
    return data;
}

function validateInput() {
    const cpInput = document.getElementById('cpValue');
    if (cpInput.value.length > 4) {
        cpInput.value = cpInput.value.slice(0, 4);
    }
}

async function filterData() {
    const cpValue = document.getElementById('cpValue').value;
    const raidChecked = document.getElementById('raidCheckbox').checked;

    if (!cpValue) {
        alert('Please enter a CP value.');
        return;
    }

    const csvText = await fetchData();
    const data = parseCSV(csvText);
    const header = data.shift(); // Remove the header

    const filteredData = data.filter(row => {
        const level = parseFloat(row[0]);
        const cp = row[4];

        if (raidChecked) {
            return (level === 20 || level === 25) && cp == cpValue;
        } else {
            return cp == cpValue;
        }
    });

    displayResults(filteredData);
}

function displayResults(data) {
    const tableBody = document.getElementById('resultsTable').getElementsByTagName('tbody')[0];
    tableBody.innerHTML = ''; // Clear previous results

    data.forEach(row => {
        const newRow = tableBody.insertRow();
        row.forEach(cell => {
            const newCell = newRow.insertCell();
            newCell.textContent = cell;
        });
    });

    if (data.length === 0) {
        const newRow = tableBody.insertRow();
        const newCell = newRow.insertCell();
        newCell.colSpan = 5;
        newCell.textContent = 'No results found.';
    }
}