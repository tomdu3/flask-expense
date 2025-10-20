// Ensure Chart.js is loaded before this script runs
document.addEventListener('DOMContentLoaded', () => {
    // Parse data passed from Jinja
    const income_vs_expense_raw = JSON.parse(document.getElementById('income_vs_expense-data').textContent);
    const income_category_data = JSON.parse(document.getElementById('income_category-data').textContent);
    const income_category_labels = JSON.parse(document.getElementById('income_category_labels-data').textContent);
    const expense_category_data = JSON.parse(document.getElementById('expense_category-data').textContent);
    const expense_category_labels = JSON.parse(document.getElementById('expense_category_labels-data').textContent);
    const over_time_expenditure = JSON.parse(document.getElementById('over_time_expenditure-data').textContent);
    const labels = JSON.parse(document.getElementById('labels-data').textContent);

    // Process income vs expense data
    const income_vs_expense_data = {};
    income_vs_expense_raw.forEach(item => {
        income_vs_expense_data[item.type] = item.amount;
    });

    // Optional: Update default scale
    if (Chart.registry && Chart.registry.scales) {
        const defaultOptions = Chart.defaults;
        if (defaultOptions.scales && defaultOptions.scales.linear) {
            defaultOptions.scales.linear.min = 0;
        }
    }

    // Initialize Income vs Expense Pie Chart
    const ctxExpense = document.getElementById('income_vs_expense');
    if (ctxExpense) {
        new Chart(ctxExpense, {
            type: 'pie',
            data: {
                labels: Object.keys(income_vs_expense_data),
                datasets: [{
                    label: "Income Vs Expenses",
                    data: Object.values(income_vs_expense_data),
                    backgroundColor: ['#E16851', '#5DA5DA', '#FAA43A', '#60BD68', '#B276B2', '#FB8267'],
                    borderWidth: 1,
                    hoverBorderColor: "black",
                    hoverBorderWidth: 2,
                    hoverBackgroundColor: 'rgba(154, 245, 140)',
                    pointHoverRadius: 5
                }],
            },
            options: {
                title: {
                    display: true,
                    text: "Income Vs Expenses",
                    fontSize: 20,
                },
                legend: {
                    position: "right",
                    labels: { fontColor: "gray" },
                    display: true,
                },
                elements: {
                    hitRadius: 3,
                }
            }
        });
    }

    // Initialize Income Categories Bar Chart
    const ctxCategory = document.getElementById('income_vs_category');
    if (ctxCategory) {
        new Chart(ctxCategory, {
            type: 'bar',
            data: {
                labels: income_category_labels,
                datasets: [{
                    label: "Categories Of Income",
                    data: income_category_data,
                    backgroundColor: ['#5DA5DA', '#E16851', '#FAA43A', '#60BD68', '#B276B2', '#FB8267'],
                    borderWidth: 1,
                    hoverBorderColor: "black",
                    hoverBorderWidth: 2,
                    hoverBackgroundColor: 'rgba(154, 245, 140)',
                    pointHoverRadius: 5
                }],
            },
            options: {
                title: {
                    display: true,
                    text: "Income Categories",
                    fontSize: 20,
                },
                legend: {
                    position: "right",
                    labels: { fontColor: "gray" },
                    display: true,
                },
                elements: {
                    hitRadius: 3,
                }
            }
        });
    }

    // Initialize Expense Categories Bar Chart
    const ctxExpenseCategory = document.getElementById('expense_vs_category');
    if (ctxExpenseCategory) {
        new Chart(ctxExpenseCategory, {
            type: 'bar',
            data: {
                labels: expense_category_labels,
                datasets: [{
                    label: "Categories Of Expenses",
                    data: expense_category_data,
                    backgroundColor: ['#E16851', '#5DA5DA', '#FAA43A', '#60BD68', '#B276B2', '#FB8267'],
                    borderWidth: 1,
                    hoverBorderColor: "black",
                    hoverBorderWidth: 2,
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top',
                        labels: {
                            boxWidth: 12
                        }
                    },
                }
            }
        });
    }

    // Initialize Over Time Expenditure Line Chart
    const ctxOverTime = document.getElementById('overtime_expenditure');
    if (ctxOverTime) {
        new Chart(ctxOverTime, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: "Expenditure Over Time",
                    data: over_time_expenditure,
                    fill: false,
                    borderColor: "rgb(255, 0, 0)",
                    lineTension: 0.1
                }]
            },
            options: {}
        });
    }
});