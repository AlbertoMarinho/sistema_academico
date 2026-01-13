// Configuração global
const API_BASE_URL = 'http://localhost:5000/api';

// Função para carregar páginas
async function loadPage(page) {
    const content = document.getElementById('content');
    
    try {
        const response = await fetch(`pages/${page}.html`);
        
        if (!response.ok) {
            throw new Error(`Erro HTTP: ${response.status}`);
        }
        
        const html = await response.text();
        content.innerHTML = html;
        
        // Remove scripts antigos
        const oldScripts = document.querySelectorAll('script[data-page]');
        oldScripts.forEach(s => s.remove());
        
        // Aguarda o DOM ser atualizado
        await new Promise(resolve => setTimeout(resolve, 100));
        
        // Carrega o script específico da página
        const script = document.createElement('script');
        script.src = `js/${page}.js?t=${Date.now()}`; // Cache busting
        script.setAttribute('data-page', page);
        script.onload = () => {
            console.log(`✅ Script ${page}.js carregado com sucesso`);
        };
        script.onerror = () => {
            console.error(`❌ Erro ao carregar script ${page}.js`);
        };
        document.body.appendChild(script);
        
    } catch (error) {
        console.error('Erro ao carregar página:', error);
        content.innerHTML = `
            <div class="container">
                <h2>Erro ao carregar página</h2>
                <p>Não foi possível carregar a página <strong>${page}.html</strong></p>
                <p style="color: red;">Erro: ${error.message}</p>
                <p>Verifique se o arquivo existe em: <code>frontend/pages/${page}.html</code></p>
                <button class="btn-primary" onclick="location.reload()">Recarregar Página</button>
            </div>
        `;
    }
}

// Funções utilitárias
function showAlert(message, type = 'success') {
    // Remove alertas antigos
    const oldAlerts = document.querySelectorAll('.alert');
    oldAlerts.forEach(alert => alert.remove());
    
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type}`;
    alertDiv.textContent = message;
    
    const container = document.querySelector('.container');
    if (container) {
        container.insertBefore(alertDiv, container.firstChild);
        
        // Auto-remove após 5 segundos
        setTimeout(() => {
            alertDiv.remove();
        }, 5000);
    }
}

function showLoading(element) {
    if (element) {
        element.innerHTML = '<div class="loading">Carregando</div>';
    }
}

function formatDate(dateString) {
    if (!dateString) return '-';
    try {
        const date = new Date(dateString);
        return date.toLocaleDateString('pt-BR');
    } catch (e) {
        return '-';
    }
}

function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.add('active');
        console.log(`✅ Modal ${modalId} aberto`);
    } else {
        console.error(`❌ Modal ${modalId} não encontrado`);
    }
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.remove('active');
        console.log(`✅ Modal ${modalId} fechado`);
    }
}

function mascaraTelefone(input) {
    let value = input.value.replace(/\D/g, ''); // Remove tudo que não é número
    
    if (value.length > 11) value = value.slice(0, 11); // Limita tamanho
    
    // Formato (XX) XXXXX-XXXX
    if (value.length > 10) {
        value = value.replace(/^(\d\d)(\d{5})(\d{4}).*/, '($1) $2-$3');
    } 
    // Formato (XX) XXXX-XXXX (fixo)
    else if (value.length > 5) {
        value = value.replace(/^(\d\d)(\d{4})(\d{0,4}).*/, '($1) $2-$3');
    } 
    // Formato (XX) ...
    else if (value.length > 2) {
        value = value.replace(/^(\d\d)(\d{0,5}).*/, '($1) $2');
    }
    
    input.value = value;
}

// Helper para aplicar máscaras automaticamente em novos inputs
function aplicarMascaras() {
    const inputsTelefone = document.querySelectorAll('input[type="tel"], #telefone');
    inputsTelefone.forEach(input => {
        input.addEventListener('input', (e) => mascaraTelefone(e.target));
    });
}

// Fechar modal ao clicar fora
document.addEventListener('click', function(event) {
    if (event.target.classList.contains('modal')) {
        event.target.classList.remove('active');
    }
});

// Log para debug
console.log('✅ app.js carregado');
console.log(`📡 API URL: ${API_BASE_URL}`);