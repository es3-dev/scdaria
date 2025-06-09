(() => {
    'use strict';

    document.addEventListener('DOMContentLoaded', function() {
        // Validación de formularios
        const forms = document.querySelectorAll('.needs-validation');
        Array.from(forms).forEach(form => {
            form.addEventListener('submit', event => {
                if (!form.checkValidity()) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });

        // Control de campos según selección de graduado
        const radioGraduadoSi = document.getElementById('graduadoSi');
        const radioGraduadoNo = document.getElementById('graduadoNo');
        const camposNoGraduado = document.getElementById('campos-no-graduado');
        
        function toggleCampos() {
            if (radioGraduadoSi && radioGraduadoNo && camposNoGraduado) {
                const esGraduado = radioGraduadoSi.checked;
                camposNoGraduado.style.display = esGraduado ? 'none' : 'block';
                
                const camposRequeridos = camposNoGraduado.querySelectorAll('[required]');
                camposRequeridos.forEach(campo => {
                    campo.required = !esGraduado;
                });
            }
        }

        if (radioGraduadoSi) radioGraduadoSi.addEventListener('change', toggleCampos);
        if (radioGraduadoNo) radioGraduadoNo.addEventListener('change', toggleCampos);
        toggleCampos();

        // Manejo de campos de asistencia
        const esGraduadoCheckbox = document.getElementById('es_graduado');
        const esGraduadoHidden = document.getElementById('es_graduado_hidden');
        const vinculacionContainer = document.getElementById('vinculacionContainer');
        const vinculacionSelect = document.getElementById('vinculacion');

        if (esGraduadoCheckbox && esGraduadoHidden && vinculacionContainer && vinculacionSelect) {
            esGraduadoCheckbox.addEventListener('change', function() {
                vinculacionContainer.style.display = this.checked ? 'none' : 'block';
                esGraduadoHidden.value = this.checked ? 'true' : 'false';
                vinculacionSelect.required = !this.checked;
                if (this.checked) {
                    vinculacionSelect.value = '';
                }
            });
        }

        // Función para copiar el link de asistencia
        const btnCopiarLinkAsist = document.getElementById('btnCopiarLinkAsist');
        const linkAsistencia = document.getElementById('linkAsistencia');
        
        async function copiarLinkAsistencia() {
            if (!btnCopiarLinkAsist || !linkAsistencia) return;
            
            try {
                await navigator.clipboard.writeText(linkAsistencia.value);
                
                // Cambiar el texto y el ícono del botón temporalmente
                const iconoOriginal = btnCopiarLinkAsist.innerHTML;
                btnCopiarLinkAsist.innerHTML = '<i class="bi bi-check-lg me-2"></i>Copiado';
                btnCopiarLinkAsist.classList.remove('btn-outline-primary');
                btnCopiarLinkAsist.classList.add('btn-success');
                
                // Restaurar el botón después de 2 segundos
                setTimeout(() => {
                    btnCopiarLinkAsist.innerHTML = iconoOriginal;
                    btnCopiarLinkAsist.classList.remove('btn-success');
                    btnCopiarLinkAsist.classList.add('btn-outline-primary');
                }, 2000);
            } catch (err) {
                console.error('Error al copiar: ', err);
                // Mostrar mensaje de error si falla la copia
                btnCopiarLinkAsist.innerHTML = '<i class="bi bi-x-circle me-2"></i>Error al copiar';
                btnCopiarLinkAsist.classList.remove('btn-outline-primary');
                btnCopiarLinkAsist.classList.add('btn-danger');
                
                setTimeout(() => {
                    btnCopiarLinkAsist.innerHTML = '<i class="bi bi-clipboard me-2"></i>Copiar';
                    btnCopiarLinkAsist.classList.remove('btn-danger');
                    btnCopiarLinkAsist.classList.add('btn-outline-primary');
                }, 2000);
            }
        }

        if (btnCopiarLinkAsist) {
            btnCopiarLinkAsist.addEventListener('click', copiarLinkAsistencia);
        }

        // Manejo de la ventana de confirmación para eliminar reunión
        let reunionIdActual = null;
        const modalConfirmacion = document.getElementById('modalConfirmacion');
        let bootstrapModal = null;
        
        if (modalConfirmacion) {
            bootstrapModal = new bootstrap.Modal(modalConfirmacion);

            // Agregar listener a todos los botones de eliminar
            document.querySelectorAll('.btn-eliminarReunion').forEach(btn => {
                btn.addEventListener('click', function(e) {
                    e.preventDefault();
                    reunionIdActual = this.dataset.reunionId;
                    bootstrapModal.show();
                });
            });

            // Listener para el botón de confirmar eliminación
            const btnConfirmarEliminar = document.getElementById('btnConfirmarEliminar');
            if (btnConfirmarEliminar) {
                btnConfirmarEliminar.addEventListener('click', function() {
                    if (reunionIdActual) {
                        const form = document.getElementById(`form-eliminar-${reunionIdActual}`);
                        if (form) {
                            form.submit();
                        }
                    }
                    bootstrapModal.hide();
                });
            }
        }
    });
})();
