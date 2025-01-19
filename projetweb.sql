-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : dim. 19 jan. 2025 à 21:24
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `projetweb`
--

-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add permission', 1, 'add_permission'),
(2, 'Can change permission', 1, 'change_permission'),
(3, 'Can delete permission', 1, 'delete_permission'),
(4, 'Can view permission', 1, 'view_permission'),
(5, 'Can add group', 2, 'add_group'),
(6, 'Can change group', 2, 'change_group'),
(7, 'Can delete group', 2, 'delete_group'),
(8, 'Can view group', 2, 'view_group'),
(9, 'Can add user', 3, 'add_user'),
(10, 'Can change user', 3, 'change_user'),
(11, 'Can delete user', 3, 'delete_user'),
(12, 'Can view user', 3, 'view_user'),
(13, 'Can add log entry', 4, 'add_logentry'),
(14, 'Can change log entry', 4, 'change_logentry'),
(15, 'Can delete log entry', 4, 'delete_logentry'),
(16, 'Can view log entry', 4, 'view_logentry'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `coach`
--

CREATE TABLE `coach` (
  `IDCoach` int(11) NOT NULL,
  `NomCoach` text NOT NULL,
  `PrenomCoach` text NOT NULL,
  `AgeCoach` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `username` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `coach`
--

INSERT INTO `coach` (`IDCoach`, `NomCoach`, `PrenomCoach`, `AgeCoach`, `password`, `username`) VALUES
(1, 'Dupont', 'Jean', 45, '', ''),
(2, 'no', 'no', 20, 'pbkdf2_sha256$600000$hqzwYo8S7LRdrkI82ff472$+6id07DkvMYxzW6dzPVlSq5Xo6c796n6AhjehTLpgGs=', 'no'),
(3, 'ge', 'greg', 20, 'pbkdf2_sha256$600000$LkRpxGxnlR5jWtp61IDdAo$cRFj3nsAiFa8w/PSRrOjrcIgvMMBaj3F6Eq5fhOeUnE=', 'greg'),
(4, 'po', 'po', 20, 'pbkdf2_sha256$600000$1lI2s1ivB1XnOd8Lztaz2k$zy27w25NrFfOAv/WMaHqp6qto/ljT19p6976x+HJY64=', 'po'),
(5, 'po', 'po', 20, 'pbkdf2_sha256$600000$NAK0dhtJjsj40o4BJKouXy$1YZKqTMMHMs1tsFE7+Pzi2bcER9iFCw9njjyyC3ahqM=', 'lo'),
(6, 'po', 'po', 20, 'pbkdf2_sha256$600000$NiWwbKaARWjzdt0GeLUh8p$sHSuXRwhQmMfEW7nUqbLv4JFj18DyBIUPtDdRAcV2lA=', 'to'),
(7, 'po', 'po', 20, 'pbkdf2_sha256$600000$gLxdj6AF8U2XJe27WIoW2P$GyF/mdikPPZ3wQsFxM6kZv/KNr2FhobQi8K6QzXOd7I=', 'la');

-- --------------------------------------------------------

--
-- Structure de la table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(4, 'admin', 'logentry'),
(2, 'auth', 'group'),
(1, 'auth', 'permission'),
(3, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Structure de la table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-11-21 19:13:55.390876'),
(2, 'auth', '0001_initial', '2024-11-21 19:13:55.786557'),
(3, 'admin', '0001_initial', '2024-11-21 19:13:55.884465'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-11-21 19:13:55.892666'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-11-21 19:13:55.900012'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-11-21 19:13:55.952663'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-11-21 19:13:56.043810'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-11-21 19:13:56.059120'),
(9, 'auth', '0004_alter_user_username_opts', '2024-11-21 19:13:56.068392'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-11-21 19:13:56.106498'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-11-21 19:13:56.110172'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-11-21 19:13:56.120393'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-11-21 19:13:56.135515'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-11-21 19:13:56.150674'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-11-21 19:13:56.163645'),
(16, 'auth', '0011_update_proxy_permissions', '2024-11-21 19:13:56.172516'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-11-21 19:13:56.185110'),
(18, 'sessions', '0001_initial', '2024-11-21 19:13:56.215917');

-- --------------------------------------------------------

--
-- Structure de la table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('7swxyhar5eyhtm1jge4d3l2gh6tu2j4r', 'eyJjb2FjaF9pZCI6OH0:1tZIAU:iJrFXN-G64sPWy7hxWXLyDME87u6X3Sj9mBpD1D0wSw', '2025-02-01 23:23:54.155820'),
('8uc8iamomiew79rux9ysts9uwgza5gw4', 'eyJjb2FjaF9pZCI6Mn0:1tZJrO:2AewRPoEPfEzhuiBR88hotVPIFcqTp6iMO1RgaEMv1w', '2025-02-02 01:12:18.301829'),
('inmbkfa8k9wvvtrbkhs4xrs3u5c382e3', 'eyJjb2FjaF9pZCI6Mn0:1tZJsW:jzv5FLjt_oxKjbkpHJJbuZ0c0vCH5xspN0fTIZqNjoQ', '2025-02-02 01:13:28.576451');

-- --------------------------------------------------------

--
-- Structure de la table `equipe`
--

CREATE TABLE `equipe` (
  `IDEquipe` int(11) NOT NULL,
  `NomEquipe` text NOT NULL,
  `RefCoach` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `equipe`
--

INSERT INTO `equipe` (`IDEquipe`, `NomEquipe`, `RefCoach`) VALUES
(1, 'Les Aigles', 1),
(2, 'Galktic', 7),
(4, 'azd', 2);

-- --------------------------------------------------------

--
-- Structure de la table `joueur`
--

CREATE TABLE `joueur` (
  `IDJoueur` int(11) NOT NULL,
  `NomJoueur` text NOT NULL,
  `PrenomJoueur` text NOT NULL,
  `refPoste` int(11) NOT NULL,
  `refRole` int(11) NOT NULL,
  `refequipe` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `joueur`
--

INSERT INTO `joueur` (`IDJoueur`, `NomJoueur`, `PrenomJoueur`, `refPoste`, `refRole`, `refequipe`) VALUES
(1, 'Arnaud', 'Noé', 1, 1, NULL),
(2, 'Meneus', 'Greg', 2, 1, NULL),
(4, 'z', 'z', 4, 1, 3),
(5, 'adz', 'azd', 4, 1, 4);

-- --------------------------------------------------------

--
-- Structure de la table `position_joueur`
--

CREATE TABLE `position_joueur` (
  `ID` int(11) NOT NULL,
  `RefTactique` int(11) NOT NULL,
  `RefJoueur` int(11) NOT NULL,
  `PositionX` float NOT NULL,
  `PositionY` float NOT NULL,
  `refRole` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `poste`
--

CREATE TABLE `poste` (
  `IDPoste` int(11) NOT NULL,
  `NomPoste` text NOT NULL,
  `DescriptionPoste` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `poste`
--

INSERT INTO `poste` (`IDPoste`, `NomPoste`, `DescriptionPoste`) VALUES
(1, 'Gardien', 'Protège le but de l’équipe.'),
(2, 'Défenseur', 'Joueur positionné dans la ligne défensive.'),
(3, 'Milieu', 'Joueur qui contrôle le milieu du terrain.'),
(4, 'Attaquant', 'Joueur principal pour marquer des buts.');

-- --------------------------------------------------------

--
-- Structure de la table `role`
--

CREATE TABLE `role` (
  `IDRole` int(11) NOT NULL,
  `NomRole` text NOT NULL,
  `DescriptionRole` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `role`
--

INSERT INTO `role` (`IDRole`, `NomRole`, `DescriptionRole`) VALUES
(1, 'Par défaut', ''),
(2, 'Gardien Libéro', 'Gardien qui joue comme dernier défenseur.'),
(3, 'Défenseur Central', 'Joueur chargé de protéger la zone devant le gardien.'),
(4, 'Arrière Latéral Attaquant', 'Défenseur qui monte sur les ailes pour participer à l\'attaque.'),
(5, 'Milieu Défensif', 'Milieu axé sur la récupération du ballon et le soutien défensif.'),
(6, 'Meneur de Jeu', 'Milieu qui contrôle le rythme du jeu avec ses passes précises.'),
(7, 'Milieu Box-to-Box', 'Milieu polyvalent, actif dans toutes les zones du terrain.'),
(8, 'Ailier Attaquant', 'Joueur de côté qui attaque et centre dans la surface adverse.'),
(9, 'Faux Neuf', 'Attaquant qui décroche pour jouer entre les lignes.'),
(10, 'Attaquant Pressing', 'Avant-centre chargé de presser les défenseurs adverses.'),
(11, 'Buteur', 'Attaquant axé sur la finition devant le but.');

-- --------------------------------------------------------

--
-- Structure de la table `stats`
--

CREATE TABLE `stats` (
  `IDStats` int(11) NOT NULL,
  `refJoueur` int(11) NOT NULL,
  `nbMatchs` int(11) NOT NULL,
  `buts` int(11) NOT NULL,
  `passeD` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `stats`
--

INSERT INTO `stats` (`IDStats`, `refJoueur`, `nbMatchs`, `buts`, `passeD`) VALUES
(1, 2, 8, 7, 2);

-- --------------------------------------------------------

--
-- Structure de la table `tactique`
--

CREATE TABLE `tactique` (
  `IdTactique` int(11) NOT NULL,
  `Nom` text NOT NULL,
  `refEquipe` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Index pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Index pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Index pour la table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Index pour la table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Index pour la table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Index pour la table `coach`
--
ALTER TABLE `coach`
  ADD PRIMARY KEY (`IDCoach`);

--
-- Index pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Index pour la table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Index pour la table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Index pour la table `equipe`
--
ALTER TABLE `equipe`
  ADD PRIMARY KEY (`IDEquipe`),
  ADD KEY `ForeignKey` (`RefCoach`);

--
-- Index pour la table `joueur`
--
ALTER TABLE `joueur`
  ADD PRIMARY KEY (`IDJoueur`),
  ADD KEY `refPoste` (`refPoste`),
  ADD KEY `refRole` (`refRole`);

--
-- Index pour la table `position_joueur`
--
ALTER TABLE `position_joueur`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `fk_reftactique` (`RefTactique`),
  ADD KEY `fk_refjoueur` (`RefJoueur`),
  ADD KEY `fk_position_joueur_refrole` (`refRole`);

--
-- Index pour la table `poste`
--
ALTER TABLE `poste`
  ADD PRIMARY KEY (`IDPoste`);

--
-- Index pour la table `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`IDRole`);

--
-- Index pour la table `stats`
--
ALTER TABLE `stats`
  ADD PRIMARY KEY (`IDStats`),
  ADD KEY `refJoueur` (`refJoueur`);

--
-- Index pour la table `tactique`
--
ALTER TABLE `tactique`
  ADD PRIMARY KEY (`IdTactique`),
  ADD KEY `fk_refequipe` (`refEquipe`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT pour la table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `coach`
--
ALTER TABLE `coach`
  MODIFY `IDCoach` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT pour la table `equipe`
--
ALTER TABLE `equipe`
  MODIFY `IDEquipe` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `joueur`
--
ALTER TABLE `joueur`
  MODIFY `IDJoueur` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT pour la table `position_joueur`
--
ALTER TABLE `position_joueur`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT pour la table `poste`
--
ALTER TABLE `poste`
  MODIFY `IDPoste` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `role`
--
ALTER TABLE `role`
  MODIFY `IDRole` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT pour la table `stats`
--
ALTER TABLE `stats`
  MODIFY `IDStats` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `tactique`
--
ALTER TABLE `tactique`
  MODIFY `IdTactique` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Contraintes pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Contraintes pour la table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `equipe`
--
ALTER TABLE `equipe`
  ADD CONSTRAINT `ForeignKey` FOREIGN KEY (`RefCoach`) REFERENCES `coach` (`IDCoach`);

--
-- Contraintes pour la table `joueur`
--
ALTER TABLE `joueur`
  ADD CONSTRAINT `joueur_ibfk_1` FOREIGN KEY (`refPoste`) REFERENCES `poste` (`IDPoste`),
  ADD CONSTRAINT `joueur_ibfk_2` FOREIGN KEY (`refRole`) REFERENCES `role` (`IDRole`);

--
-- Contraintes pour la table `position_joueur`
--
ALTER TABLE `position_joueur`
  ADD CONSTRAINT `fk_position_joueur_refrole` FOREIGN KEY (`refRole`) REFERENCES `role` (`IDRole`),
  ADD CONSTRAINT `fk_refjoueur` FOREIGN KEY (`RefJoueur`) REFERENCES `joueur` (`IDJoueur`) ON DELETE CASCADE,
  ADD CONSTRAINT `fk_reftactique` FOREIGN KEY (`RefTactique`) REFERENCES `tactique` (`IdTactique`) ON DELETE CASCADE;

--
-- Contraintes pour la table `stats`
--
ALTER TABLE `stats`
  ADD CONSTRAINT `stats_ibfk_1` FOREIGN KEY (`refJoueur`) REFERENCES `joueur` (`IDJoueur`);

--
-- Contraintes pour la table `tactique`
--
ALTER TABLE `tactique`
  ADD CONSTRAINT `fk_refequipe` FOREIGN KEY (`refEquipe`) REFERENCES `equipe` (`IDEquipe`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
