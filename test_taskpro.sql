USE taskpro_test;

-- Limpiar tablas en orden correcto para evitar violaciones de FK
DELETE FROM tareas;
DELETE FROM usuarios;

-- Insertar usuarios
INSERT INTO usuarios (nombre, email, password, fecha_registro) VALUES
('Ana Torres', 'ana@example.com', SHA2('ana123', 256), NOW()),
('Carlos Méndez', 'carlos@example.com', SHA2('carlos123', 256), NOW()),
('Lucía Rojas', 'lucia@example.com', SHA2('lucia123', 256), NOW());

-- Insertar tareas referenciando los ID reales mediante subconsultas
INSERT INTO tareas (titulo, descripcion, fecha_creacion, fecha_vencimiento, estado, creada_por, asignada_a)
VALUES
('Planificar sprint', 'Organizar backlog para el próximo sprint.', NOW(), DATE_ADD(NOW(), INTERVAL 7 DAY), 'Pendiente',
 (SELECT id FROM usuarios WHERE email = 'ana@example.com'),
 (SELECT id FROM usuarios WHERE email = 'carlos@example.com')),

('Revisar código', 'Hacer revisión de pull requests pendientes.', NOW(), DATE_ADD(NOW(), INTERVAL 3 DAY), 'En Progreso',
 (SELECT id FROM usuarios WHERE email = 'carlos@example.com'),
 (SELECT id FROM usuarios WHERE email = 'ana@example.com')),

('Actualizar documentación', 'Actualizar el manual de usuario y el README.', NOW(), DATE_ADD(NOW(), INTERVAL 5 DAY), 'Pendiente',
 (SELECT id FROM usuarios WHERE email = 'lucia@example.com'),
 (SELECT id FROM usuarios WHERE email = 'lucia@example.com'));