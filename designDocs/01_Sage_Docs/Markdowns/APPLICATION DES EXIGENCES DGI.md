![](_page_0_Picture_1.jpeg)

# *Contrôles des comptabilités informatisées*

*Application des exigences DGI dans les lignes Sage Start, 30 et 100*

Instruction 13L-1-06 <sup>n</sup>°12 du <sup>24</sup> janvier 2006

![](_page_0_Picture_5.jpeg)

| Composition du progiciel |  |  |
|--------------------------|--|--|
|--------------------------|--|--|

| Votre progiciel est composé d'un boîtier de rangement comprenant<br>: |
|-----------------------------------------------------------------------|
| ‰<br>le cédérom sur lequel est enregistré le programme,               |
| ‰<br>la documentation électronique, présente sur le cédérom.          |

#### **Propriété & Usage**

Tout usage, représentation ou reproduction intégral ou partiel, fait sans le consentement de Sage est illicite (Loi du 11 Mars 1957 - Loi du 3 Juillet 1985). Ils constitueraient une contrefaçon sanctionnée par les articles 425 et suivants du Code Pénal.

Tous droits réservés dans tous pays.

Logiciel original développé par Sage. Documentation Sage.

Toute utilisation, à quelque titre que ce soit, non autorisée dans le cadre de la convention de licence, est strictement interdite sous peine de sanctions pénales (Loi du 3 Juillet 1985, Art. 46).

#### **Conformité & Mise en garde**

Compte tenu des contraintes inhérentes à la présentation sous forme de manuel électronique, les spécifications visées dans la présente documentation constituent une illustration aussi proche que possible des spécifications. Il appartient au client, parallèlement à la documentation, de mettre en œuvre le progiciel pour permettre de mesurer exactement l'adéquation de ses besoins aux fonctionnalités. Il est important, pour une utilisation sûre et opérationnelle du progiciel, de lire préalablement la documentation.

#### **Evolution**

La documentation correspond à la version référencée. Entre deux versions, des mises à jour du logiciel peuvent être opérées sans modification de la documentation. Toutefois, un additif peut être joint à la documentation existante pour présenter les modifications et améliorations apportées à ces mises à jour.

#### **Marques**

Start, Ligne 30, Ligne 100, Intégrale, et Ligne 1000 sont des marques déposées appartenant à Sage.

Windows 98 SE, Windows 2000, Windows 2003 Server, Windows XP, les logiciels Microsoft Excel, Microsoft Word, Microsoft Outlook, Internet Explorer et gamme Office sont des marques déposées de Microsoft Corporation.

Macintosh, MAC/OS est une marque déposée de Apple Computer Inc.

SAGE SAS - Société par Actions Simplifiée au capital social de 500.000 euros Siège social : 10, rue Fructidor 75017 Paris - 313 966 129 R.C.S. Paris

La société Sage est locataire-gérante des sociétés Sage Coala, Adonix, Adonix Applications & Services et Logan SA informatique.

## Sommaire

| Introduction                                                                   | 3      |
|--------------------------------------------------------------------------------|--------|
| Processus de validation des<br>écritures comptables                            | 4      |
| Processus de clôtures                                                          |        |
| périodiques<br>                                                                | 5      |
| Sage comptabilité                                                              | 6      |
| Processus de clôtures                                                          |        |
| exercices<br>                                                                  | 12     |
| Contrôles préalables                                                           | 13     |
| Le fichier comptable doit être impérativement en<br>accès mono utilisateur<br> | 13     |
| Contrôle des données comptables                                                | 15     |
| Clôture de l'exercice                                                          | 15     |
| Impression des documents annuels au                                            |        |
| format PDF<br>                                                                 | 17     |
| Sélection du format d'impression<br>                                           | 18     |
| Emplacement des fichiers PDF<br>                                               | 20     |
| Sauvegarde des impressions générées                                            | <br>21 |
|                                                                                |        |
| Archivage des données de la<br>comptabilité<br>                                | 22     |
|                                                                                |        |

| Permanence du chemin de<br>révision<br>                                           |    |
|-----------------------------------------------------------------------------------|----|
| Pont comptable des applications en<br>amont                                       | 26 |
| Gestion commerciale, et Start Compta<br>facture, Saisie de caisse décentralisée26 |    |
| Sélection du format d'impression28<br>Emplacement des fichiers PDF<br>29          |    |
| Moyens de paiement<br>30                                                          |    |
| Sélection du format d'impression31<br>Emplacement des fichiers PDF<br>32          |    |
| Immobilisations33                                                                 |    |
| Sélection du format d'impression34<br>Emplacement des fichiers PDF<br>35          |    |
| Paie SAGE pour Windows37                                                          |    |
| Sélection du format d'impression38<br>Emplacement des fichiers PDF<br>39          |    |
| Paie pour Macintosh<br>40                                                         |    |
| Sélection du format d'impression41                                                |    |
| Emplacement des fichiers PDF<br>42                                                |    |
| Intangibilité des pièces                                                          |    |
| commerciales<br>                                                                  | 43 |
| Gestion commerciale, Start Compta                                                 |    |
| facture, Saisie de caisse décentralisée44<br>Sélection du journal de vente<br>45  |    |

| Archivage dans les                                                                         |                |
|--------------------------------------------------------------------------------------------|----------------|
| applications périphériques                                                                 | 46             |
| Gestion commerciale, Start Compta<br>facture, Saisie de caisse décentralisée               | <br>47         |
| Impression des journaux<br>Impression des factures                                         | 47<br>50       |
| Moyens de paiement<br><br>Sélection du format d'impression<br>Emplacement des fichiers PDF | 55<br>56<br>57 |
| Immobilisations<br>                                                                        | 58             |
| Sélection du format d'impression<br>Emplacement des fichiers PDF                           | 59<br>60       |
| Etats comptables et fiscaux<br>                                                            | 62             |
| Sélection du format d'impression<br>Emplacement des fichiers PDF                           | 62<br>63       |
| Chronologie des écritures en                                                               |                |
| comptabilité64                                                                             |                |
| Documentations des logiciels                                                               | 66             |

# Introduction

L'instruction 13L-1-06 n° 12 du 24 janvier 2006 publiée au Bulletin Officiel des Impôts et relative au contrôle des comptabilités informatisées impose un certain nombre d'exigences aux entreprises françaises tenant leur comptabilité au moyen d'un système informatisé afin qu'elle soit réputée sincère, régulière et probante.

Les applications Sage Ligne 100, Ligne 30 et Start proposent les fonctionnalités métiers permettant de répondre aux exigences de la DGI. Ce guide pratique décrit comment répondre à ces exigences au travers de votre application Sage de manière illustrée.

Dans ce manuel, toutes les indications et manipulations indiquées sont réalisables sur les applications Ligne 100, Ligne 30 et Start. Nous parlerons donc de Sage comptabilité, Sage Gestion commerciale, Sage Saisie de caisse décentralisé, Sage Immobilisations, Sage Moyens de Paiement, Sage Paie pour Macintosh sans faire référence à la ligne de produit sauf cas particulier.

Les exigences de la DGI en matière de comptabilités informatisées s'articulent autour des 5 grandes familles suivantes :

- Processus de validation des écritures comptables,
- Processus de clôtures périodiques et d'exercices,
- Processus de comptabilisation des pièces des applications en amont de la comptabilité,
- Documentation de l'application,
- Conservation et archivage des documents comptables.

![](_page_4_Picture_11.jpeg)

*A chaque en-tête de chapitre sont mentionnés dans un encadré les paragraphes de l'instruction correspondants* 

# Processus de validation des écritures comptables

**Paragraphes 19 à 24 de l'instruction – Principe du caractère intangible ou de l'irréversibilité des écritures comptables** 

#### Î Historisation des écritures « brouillard »

**Un traitement informatique volontaire et irréversible de validation des écritures comptables, qui s'oppose à la saisie en mode « brouillard », interdit toute modification ou suppression des enregistrements ayant fait l'objet de ce traitement assurant ainsi l'intangibilité des enregistrements comptables (PCG 420-5).** 

#### Î Attributs des écritures validées

**Chaque écriture validée doit présenter les attributs non modifiables suivants : date de valeur comptable ou date de validation, référence de la pièce justificative (PCG 420-2) afin d'assurer la permanence du chemin de révision (PCG 410-3).** 

## Processus de clôtures périodiques

**Paragraphes 25 à 29 de l'instruction – Principe d'une procédure de clôture périodique des enregistrements chronologiques** 

#### Î Clôture périodique

**Il s'agit d'un processus figeant la chronologie et garantissant l'intangibilité des enregistrements comptables. Il doit être mis en œuvre au plus tard avant l'expiration de la période suivante.** 

**La période est l'intervalle de temps durant lequel les écritures sont enregistrées en vue de leur centralisation (mois ou trimestre par exemple) afin d'établir des situations intermédiaires en cours d'exercice comptable. D'un point de vue pratique il est vivement conseillé de procéder à la clôture après envoi de la déclaration de TVA.** 

### Î Comptabilisation d'un événement intervenant sur une période déjà clôturée

**Cette opération sera enregistrée avec une date de comptabilisation égale à la date du premier jour de la période non encore clôturée avec mention expresse de sa date de survenance.** 

## Sage comptabilité

Dans votre application **Sage Comptabilité**, une écriture est provisoire tant que la période comptable à laquelle elle appartient est ouverte.

Pour répondre à l'exigence DGI garantissant l'intangibilité des enregistrements comptables, il convient par conséquent de lancer le processus de clôture périodique.

*Clôture périodique* : il s'agit d'un processus irréversible figeant une période (ni création de nouvelles écritures sur la période clôturée ni modification / suppression).

Le lancement de ce traitement est irréversible (un message d'alerte sur l'écran de lancement vous le signale).

![](_page_7_Picture_6.jpeg)

*La responsabilité de toute modification par SGBD vous incombe.* 

Les informations et données saisies par l'Utilisateur du progiciel et stockées dans les bases de données relationnelles ne doivent pas faire l'objet de modifications ultérieures.

Toute modification intervenant sur les informations et données stockées après la saisie initiale est de la responsabilité de l'Utilisateur ; Sage ne saurait être tenue pour responsable à ce titre.

La saisie d'une nouvelle écriture n'étant pas permise sur une période clôturée, elle sera saisie à la date du premier jour de la période non encore clôturée et nous vous conseillons de saisir la date de survenance dans le libellé de l'écriture.

![](_page_7_Picture_11.jpeg)

*Cette date de survenance est indicative ; en aucun cas elle est prise en compte dans les processus d'exploitation ou les éditions standards.* 

![](_page_7_Picture_13.jpeg)

*La clôture définitive des journaux nécessite impérativement de sauvegarder le fichier comptable avant d'exécuter cette commande.* 

Vérifier que le mode assistant est activé, dans le menu *Fenêtre* la ligne Mode Assistant doit comporter une coche, dans le cas contraire il suffit de cliquer sur la ligne pour l'activer.

Lancez la fonction de clôture d'exercice de votre application Sage Comptabilité par la commande *Traitement* / *Clôture de journaux* ; l'assistant de clôture est proposé :

![](_page_8_Figure_1.jpeg)

Sélectionnez l'option « Totale » puis cliquez sur le bouton suivant.

#### **Sélection des journaux**

![](_page_8_Figure_4.jpeg)

#### *Sélectionner par un simple clic les types journaux à clôturer totalement*

Aucun journal n'est par défaut sélectionné. Cliquez sur le bouton *Tout sélectionner*

![](_page_9_Picture_3.jpeg)

*Les journaux de situation ne peuvent pas être clôturés et ne sont pas affichés dans cet écran.* 

#### *Sélectionner la période limite à clôturer.*

Ce menu local non éditable présente la liste des périodes de l'exercice. Par défaut, il affiche le mois précédant le mois en cours.

#### *La période limite à clôturer correspond en principe à la période de déclaration de votre TVA.*

Exemple vous télé déclarez votre TVA le 21/05 vous devez clôturer les écritures jusqu'au 30/04.

![](_page_9_Picture_9.jpeg)

*Le bouton Suivant devient accessible si au moins un journal est sélectionné et si la date limite est définie.* 

#### **Impression des journaux**

![](_page_9_Figure_12.jpeg)

#### *Souhaitez-vous imprimer ?*

- **Les journaux non encore imprimés** : les journaux non encore édités appartenant à la période définie sont édités. Vous pouvez conserver cette sélection.
- **Tous les journaux** : tous les journaux du 1er mois de l'exercice au mois sélectionné sont édités.

#### *Bouton Fin*

Le bouton **Suivant** change de nom et lance la clôture des journaux en fonction des paramètres saisis. Il ne devient accessible que si au moins un journal est sélectionné et si la date limite est définie.

Le lancement de ce traitement est irréversible (un message d'alerte sur l'écran de lancement vous le signale).

![](_page_10_Picture_4.jpeg)

*La responsabilité de toute modification par SGBD vous incombe.* 

#### **Sélection du format d'impression**

![](_page_10_Picture_7.jpeg)

![](_page_10_Picture_8.jpeg)

*Cochez impérativement l'option Impression dans un fichier PDF et cliquez sur le bouton [OK].* 

La tenue d'une comptabilité informatisée est soumise à des obligations en termes de conservation et de présentation des documents comptables, récapitulées dans l'instruction de la Direction Générale des Impôts n° 13 L-1-06 en date du 24 janvier 2006, obligations que chaque Utilisateur se doit de respecter. La fenêtre Impression permet d'imprimer les documents au format PDF. Il incombe à l'utilisateur de les archiver et de les conserver sur un support pérenne et ainsi de respecter ces obligations.

#### *Equivalent sur Macintosh*

![](_page_11_Figure_2.jpeg)

#### **Emplacement des fichiers PDF**

![](_page_11_Figure_4.jpeg)

Nous vous proposons d'adopter l'arborescence suivante : à l'endroit de stockage de votre fichier comptable, créer un répertoire par année avec deux sous répertoires, un destiné à l'enregistrement des impressions mensuelles ou trimestrielles, un autre pour stocker les impressions annuelles et un sous répertoire par applications générant des écritures dans la comptabilité (Gestion commerciale, Saisie de caisse décentralisé, Moyens de paiement, Etats comptables et fiscaux, Paie…).

#### *Exemple :*

![](_page_12_Picture_2.jpeg)

![](_page_12_Picture_3.jpeg)

*Il est indispensable de limiter l'accès en lecture seule aux utilisateurs non habilités afin d'éviter tout risque de suppression.* 

Après sélection du répertoire «Documents mensuels 2006 » modifier le nom de fichier en indiquant la période concernée par la clôture.

#### *Exemple :*

*Si on procède à une clôture mensuelle du mois d'avril, le nom du fichier pdf sera : Impressions\_des\_journaux\_0406.pdf.* 

## Processus de clôtures exercices

#### Î Clôture exercice :

**« […] au terme d'une période de 12 mois […], il doit être obligatoirement procédé à la clôture de l'exercice. ». C'est à la clôture annuelle que sont établis les comptes annuels au vu des enregistrements comptables et d'inventaire : bilan, compte de résultat et annexe forment un tout indissociable.** 

## Contrôles préalables

#### Le fichier comptable doit être impérativement en accès mono utilisateur

#### Vérification des utilisateurs connectés

Si vous utilisez l'application en réseau vérifiez que vous êtes le seul utilisateur sur la base de données, lancez le menu *Configuration système et partage* du menu *Fichier* et sélectionnez le volet « Utilisateurs connectés ».

Le volet **Utilisateurs connectés** permet de visualiser, le cas échéant, les noms des utilisateurs connectés aux différents fichiers ouverts.

![](_page_14_Picture_6.jpeg)

Pour ouvrir ce volet cliquez sur l'onglet **Utilisateurs connectés** ou sur le bouton cicontre pour la version Macintosh du programme.

Cette fiche est vide si le mode d'accès n'est pas avec le Serveur Sage.

![](_page_14_Figure_9.jpeg)

Lorsqu'un ou plusieurs utilisateurs sont connectés, le bouton **Envoyer un message** permet d'accéder à la fenêtre de saisie d'un message.

![](_page_14_Picture_11.jpeg)

*Le bouton n'est pas accessible si l'utilisateur sélectionné sur la liste est le poste de travail.* 

Sélectionnez préalablement la ou les lignes des utilisateurs destinataires du message et cliquer sur le bouton *Envoyer un message.*

![](_page_15_Picture_1.jpeg)

![](_page_15_Picture_2.jpeg)

*Le programme ne vous prévient pas si un destinataire n'est pas en mesure de recevoir votre message.* 

Vous disposez de 255 caractères alphanumériques pour rédiger le texte de votre message, cliquer ensuite sur le bouton *Envoyer*.

#### Passage de la base en mono utilisateur

Après déconnexion des utilisateurs lancer la fonction *Autorisations d'accès* du menu *Fichier*

![](_page_15_Picture_7.jpeg)

Sélectionner l'option *Mono-utilisateur* dans le menu *Accès*.

#### Contrôle des données comptables

Imprimer au préalable une balance générale, Bilan, Compte de résultat et vérifier que les données correspondent à votre liasse fiscale.

#### Que faire en cas de différence :

- Le montant du résultat de la liasse est différent de la balance : Vérifier que les OD passées dans les Etats comptables et fiscaux ont bien été comptabilisées
- Les totaux du bilan/compte de résultat de la liasse et de l'état préparatoire sont différents. C'est probablement lié à un compte non défini dans une fourchette. Vous pouvez comparer les totaux intermédiaires pour isoler les rubriques concernées.

La comptabilité propose par ailleurs des outils de contrôles qui vous permettent d'isoler rapidement ces erreurs de paramétrage. Veuillez lancer la fonction *Contrôles de paramétrage* accessible à partir du Menu *Etat / Analyse et contrôle*.

L'écran suivant est proposé :

![](_page_16_Picture_8.jpeg)

Veuillez sélectionner dans la liste *Type de contrôle* l'état que vous souhaitez vérifier. Vous obtenez un état qui référence les erreurs de paramétrage comme les comptes en doublon ou non référencés. Après rectification et vérification vous pouvez passer à l'étape suivante.

### Clôture de l'exercice

**Avant tout traitement veuillez procéder obligatoirement à une sauvegarde de votre base comptable** (fichier avec une extension .mae). Il est également indispensable de procéder à un test de restauration afin de vérifier le bon fonctionnement de la procédure de sauvegarde.

Lancez la fonction de clôture d'exercice de votre application Sage Comptabilité par la commande *Traitement* / *Fin d'exercice.* 

![](_page_17_Picture_1.jpeg)

Cliquer sur le bouton **Clôture de l'exercice** de la barre d'outils **Fonctions avancées** revient à activer cette commande.

![](_page_17_Picture_3.jpeg)

La clôture ne peut s'effectuer que sur le premier exercice non clôturé. Il faut qu'il soit actif pour pouvoir lancer la commande.

Clôturer un exercice a pour conséquence d'interdire toute saisie ou modification des écritures enregistrées. Il ne sera pas possible d'importer des écritures. La mise à jour de l'exercice par l'intermédiaire d'autres applications (la gestion commerciale ou la paie) ne sera également plus possible.

## Impression des documents annuels au format PDF

![](_page_18_Picture_2.jpeg)

*Si vous êtes soumis à la gestion des normes IFRS il est indispensable d'imprimer les documents à la norme nationale. Cliquer sur le bouton Norme nationale de la barre d'outils norme. La norme sélectionnée est rappelée dans la barre de statut au bas de la fenêtre de l'application.* 

![](_page_18_Picture_4.jpeg)

Liste des documents à imprimer

- Grand livre général
- Grand livre tiers
- Journal + Journal général
- Balance générale
- Balance tiers
- Bilan

#### • Compte de résultat

![](_page_19_Picture_2.jpeg)

*Pour les utilisateurs des Etats comptables et fiscaux Sage, nous vous invitons à utiliser les fonctions d'archivage de la liasse. Si vous êtes soumis aux IFRS, nous vous invitons également à imprimer les documents en activant la norme IFRS.* 

*Vous trouverez ci-joint la description pour imprimer le grand livre, la même procédure devra être dupliquée pour les autres documents à imprimer.* 

Menu *Etat*, sélectionnez *Grand livre des comptes,* sélectionnez dans la liste déroulante *Type d'état* le modèle *Base ou Développé* et cliquez sur le bouton [OK]

#### Sélection du format d'impression

![](_page_19_Picture_7.jpeg)

![](_page_19_Picture_8.jpeg)

*Cochez impérativement l'option Impression dans un fichier PDF et cliquez sur le bouton [OK].* 

La tenue d'une comptabilité informatisée est soumise à des obligations en termes de conservation et de présentation des documents comptables, récapitulées dans l'instruction de la Direction Générale

des Impôts n° 13 L-1-06 en date du 24 janvier 2006, obligations que chaque Utilisateur se doit de respecter.

La fenêtre Impression permet d'imprimer les documents au format PDF. Il incombe à l'utilisateur de les archiver et de les conserver sur un support pérenne et ainsi de respecter ces obligations.

#### *Equivalent sur Macintosh*

![](_page_20_Figure_4.jpeg)

## Emplacement des fichiers PDF

![](_page_21_Picture_2.jpeg)

Après sélection du répertoire «Documents annuels 2006 » modifier le nom de fichier en indiquant la période concernée par la clôture:

#### *Exemple :*

*Grand-livre\_des\_comptes\_2006.pdf* 

![](_page_21_Picture_6.jpeg)

*Veuillez suivre cette procédure pour l'ensemble des autres états à imprimer.* 

## Sauvegarde des impressions générées

Veuillez procéder à la sauvegarde du fichier \*.pdf généré afin de le conserver en archive sur un support pérenne de votre choix (exemple CD ou DVD non réinscriptibles…).

**« Les entreprises doivent conserver les livres, registres, documents […] sous une forme dématérialisée dans un format immédiatement lisible. »** 

**Le délai général de conservation est de 6 ans et de 3 ans minimum sur support informatique.**

![](_page_22_Picture_5.jpeg)

*Vous pouvez bien entendu imprimer le fichier pdf afin de conserver une archive papier.* 

# Archivage des données de la comptabilité

**Paragraphes 100 de l'instruction : …« La date de l'archivage correspond généralement, non pas à la date de la clôture de l'exercice, mais à celle de la clôture réelle des comptes, soit une date proche de la date de dépôt des déclarations. »** 

Lancez la fonction *Exporter* de la comptabilité *Format ligne 100 et 30, HTML*… du menu *Fichier.* 

![](_page_23_Picture_4.jpeg)

Cliquer sur le bouton **Export/format Ligne 100 et 30, HTML** de la barre d'outils **Fonctions avancées** revient à activer cette commande.

Sélectionnez un format de sélection ou créez-le. Le tableau ci-dessous indique les paramètres à y mentionner

#### *Vous ne gérer pas les IFRS*

| Fichier   | Champ | De     | à |
|-----------|-------|--------|---|
| Ecritures | Norme | Toutes |   |

Vous gérer les IFRS, nous vous conseillons de générer deux archives distinctes, une pour chaque norme en utilisant les formats de sélection ci-dessous :

## *Archivage en norme nationale*

| Fichier   | Champ | De        | à |
|-----------|-------|-----------|---|
| Ecritures | Norme | Nationale |   |

## *Archivage en norme IFRS*

| Fichier   | Champ | De   | à |
|-----------|-------|------|---|
| Ecritures | Norme | IFRS |   |

Nous illustrerons le cas d'une comptabilité non soumise aux IFRS. Le format de sélection présente la forme suivante :

![](_page_24_Picture_1.jpeg)

Cliquez sur le bouton [Exporter]

![](_page_24_Picture_3.jpeg)

Vous obtenez la fenêtre suivante,

![](_page_24_Figure_5.jpeg)

Dans la zone type sélectionner l'option « Format XML (\*.xml), veuillez indiquer dans la zone *Nom de fichier* les coordonnées appropriées.

#### *Exemple :*

*Archivage comptabilité 2006.* 

Cliquer sur le bouton [Enregistrer] pour valider le traitement.

#### Sauvegarde du fichier généré

Veuillez procéder à la sauvegarde du fichier \*.xml généré afin de le conserver en archive sur un support pérenne de votre choix (exemple CD ou DVD non réinscriptibles…)

**Paragraphes 96 de l'instruction : …« Une procédure d'archivage vise les objectifs suivants : copier sur support informatique pérenne ces documents et données, de manière à permettre leur exploitation indépendamment du système… »** 

## Permanence du chemin de révision

**Dans les applications en amont de la comptabilité : lorsqu'il existe un processus de comptabilisation (pont des achats, des ventes, des stocks, de la production, des paies, des immobilisations, des écritures bancaires, de trésorerie …), il doit exister un outil de simulation permettant à l'utilisateur de contrôler les écritures comptables générées avant de lancer le traitement de comptabilisation réelle (traitement définitif irréversible interdisant la modification / suppression des éléments d'origine qui prennent le statut « comptabilisé »).** 

**Chacune des applications périphériques de la Sage comptabilité proposent une fonction d'impression du journal comptable répondant ainsi à cette obligation. Nous vous conseillons par ailleurs d'archiver également les journaux comptables émis à partir de ces différentes applications.** 

**Vous trouverez ci-dessous la description de ce processus pour l'ensemble des applications concernées.** 

## Pont comptable des applications en amont

## Gestion commerciale, et Start Compta facture, Saisie de caisse décentralisée

Avant la mise à jour comptable des écritures dans la comptabilité veuillez procéder à l'impression du journal comptable correspondant.

Lancez la fonction Journaux comptables du menu Etat, la fenêtre suivante est proposée :

![](_page_27_Picture_5.jpeg)

#### *Domaine :*

Liste déroulante permettant la sélection des états comptables :

- **Factures des ventes** : (valeur par défaut) permet l'impression des états relatifs au journal des ventes.
- **Factures des achats** : permet l'impression des états relatifs au journal des achats.
- **Règlements clients** : permet l'impression des états relatifs au journal des règlements des ventes.
- **Règlements fournisseurs** : permet l'impression des états relatifs au journal des règlements des achats.

Sélectionnez le domaine en fonction de votre gestion.

![](_page_27_Picture_13.jpeg)

*L'opération d'impression des journaux comptables correspondant doit être répétée pour chacun des domaines gérés.* 

#### *Journal analytique*

Liste déroulante permettant d'imprimer le journal analytique correspondant au plan désigné en ventilation. Sélectionnez l'option appropriée.

#### *Etat des pièces*

Liste déroulante permettant de prendre en compte, lors des impressions, soit les pièces comptabilisées, soit les pièces non comptabilisées. Sélectionnez l'option par défaut « pièces non comptabilisées »

#### *Date de / à*

Zones permettant de sélectionner la période à prendre en compte pour l'impression. Par défaut, le programme reprend l'année civile correspondant à la date du micro-ordinateur. Veuillez sélectionner la période correspondante à la comptabilisation de vos factures.

Ces zones comportent un bouton permettant d'ouvrir un calendrier et de sélectionner facilement une date.

Cliquez sur le bouton [OK]

#### Sélection du format d'impression

![](_page_29_Figure_2.jpeg)

![](_page_29_Figure_3.jpeg)

## *Cochez impérativement l'option Impression dans un fichier PDF et cliquez sur le bouton [OK].*

La tenue d'une comptabilité informatisée est soumise à des obligations en termes de conservation et de présentation des documents comptables, récapitulées dans l'instruction de la Direction Générale des Impôts n° 13 L-1-06 en date du 24 janvier 2006, obligations que chaque Utilisateur se doit de respecter. La fenêtre Impression permet d'imprimer les documents au format PDF. Il incombe à l'utilisateur de les archiver et de les conserver sur un support pérenne et ainsi de respecter ces obligations.

#### *Equivalent sur Macintosh*

![](_page_30_Picture_2.jpeg)

## Emplacement des fichiers PDF

![](_page_30_Picture_4.jpeg)

Après sélection du répertoire *Documents gestion commerciale 2006*, modifiez le nom de fichier en indiquant la période concernée par la mise à jour comptable:

#### *Exemple :*

*Journaux\_ventes\_Gescom\_010106\_150106.pdf.* 

Après la mise à jour comptable des écritures dans votre logiciel de comptabilité et avant la procédure de clôture partielle décrite dans le chapitre « Principe de permanence du chemin de révision », vérifiez la concordance des informations.

## Moyens de paiement

Avant la mise à jour comptable des écritures dans la comptabilité veuillez procéder à l'impression du journal comptable correspondant.

Lancez la fonction *Mise à jour de la comptabilité* du menu *Traitement*, la fenêtre suivante est proposée :

![](_page_31_Picture_4.jpeg)

Sélectionner l'option « Edition du journal comptable ».

#### *Date limite*

Indiquez la date de fin de vos écritures.

#### *Etat des échéances*

Liste déroulante permettant de prendre en compte, lors des impressions, soit les pièces comptabilisées, soit les pièces non comptabilisées. Sélectionnez l'option « pièces non comptabilisées »

Cliquez sur le bouton [Mise à jour directe].

#### Sélection du format d'impression

![](_page_32_Picture_2.jpeg)

![](_page_32_Picture_3.jpeg)

*Cochez impérativement l'option* **Impression dans un fichier PDF** *et cliquez sur le bouton [OK].* 

La tenue d'une comptabilité informatisée est soumise à des obligations en termes de conservation et de présentation des documents comptables, récapitulées dans l'instruction de la Direction Générale des Impôts n° 13 L-1-06 en date du 24 janvier 2006, obligations que chaque Utilisateur se doit de respecter. La fenêtre Impression permet d'imprimer les documents au format PDF. Il incombe à l'utilisateur de les archiver et de les conserver sur un support pérenne et ainsi de respecter ces obligations.

#### *Equivalent sur Macintosh*

![](_page_33_Figure_2.jpeg)

## Emplacement des fichiers PDF

![](_page_33_Figure_4.jpeg)

Après sélection du répertoire *Moyens de paiement 2006* modifiez le nom de fichier en indiquant la période concernée par la mise à jour comptable des écritures:

#### *Exemple :*

*Journaux\_comptables\_MDP\_150106.pdf.* 

Après la mise à jour comptable des écritures dans votre logiciel de comptabilité, vérifiez la concordance des informations.

## Immobilisations

Avant la mise à jour comptable des écritures dans la comptabilité veuillez procéder à l'impression du journal comptable correspondant.

Lancez la fonction *Journaux comptables* du menu *Etat*, la fenêtre suivante est proposée :

![](_page_34_Picture_4.jpeg)

#### *Type*

Liste déroulante permettant de choisir entre :

- Exercice **:** comptabilisation annuelle des écritures en date de fin d'exercice,
- Mois : comptabilisation mensuelle avec régularisation éventuelle sur le dernier mois de l'exercice,
- Situation : impression du journal comptable à une date différente de celle de la fin d'exercice. Les valeurs obtenues seront calculées en fonction de la date de situation saisie dans les listes déroulante

#### *Période.*

Sélectionnez l'option conformément à la fréquence de mise à jour des écritures, mensuelle, annuelle. Si vous comptabilisez vos écritures avec une fréquence différente (ex : mise à jour trimestrielle) veuillez sélectionner l'option « Situation ».

#### *Exercice*

Liste déroulante permettant de sélectionner l'exercice sur lequel portera l'impression. Par défaut, le dernier exercice sur lequel un calcul des amortissements (fonction *Traitement / Calcul des amortissements*) a été lancé est proposé.

#### *Période de / à*

Dans le cadre de l'impression d'un journal de type Mois ou Situation, saisissez dans les colonnes *De*  et *à* les dates de la situation demandée.

#### *Ecritures*

Laissez la valeur par défaut « Dotations à comptabiliser ».

Cliquez sur le bouton [OK]

#### Sélection du format d'impression

![](_page_35_Picture_5.jpeg)

![](_page_35_Picture_6.jpeg)

*Cochez impérativement l'option* **Impression dans un fichier PDF** *et cliquez sur le bouton [OK].* 

La tenue d'une comptabilité informatisée est soumise à des obligations en termes de conservation et de présentation des documents comptables, récapitulées dans l'instruction de la Direction Générale des Impôts n° 13 L-1-06 en date du 24 janvier 2006, obligations que chaque Utilisateur se doit de respecter. La fenêtre Impression permet d'imprimer les documents au format PDF. Il incombe à l'utilisateur de les archiver et de les conserver sur un support pérenne et ainsi de respecter ces obligations.

#### *Equivalent sur Macintosh*

![](_page_36_Figure_2.jpeg)

#### Emplacement des fichiers PDF

Après sélection du répertoire «Immobilisations 2006 », modifiez le nom de fichier en indiquant la période concernée par la mise à jour comptable des écritures.

![](_page_36_Figure_5.jpeg)

Après sélection du répertoire «Immobilisations 2006 » modifiez le nom de fichier en indiquant la période concernée par la mise à jour comptable des écritures:

#### *Exemple :*

*Journal\_comptable\_Immo\_010106\_310106.pdf.* 

Vérifiez la concordance des informations avec la comptabilité.

Cette opération doit être répétée autant de fois que la fréquence des mises à jour comptable.

## Paie SAGE pour Windows

Avant la passation comptable des écritures de Paie dans la comptabilité, veuillez procéder à l'impression du journal de Paie correspondant.

Lancez la fonction *Passation comptable* du menu *Annexes*, la fenêtre suivante est proposée :

![](_page_38_Figure_4.jpeg)

Cette fonction permet de lancer directement la passation comptable et permet aussi d'éditer le journal de Paie correspondant.

La fenêtre de sélection se présente comme suit :

## *Comptabilisation au*

La date proposée par défaut est celle du dernier jour du mois en cours, il est possible de la modifier. Par défaut, sont repris tous les bulletins non encore comptabilisés.

#### *Reprise des bulletins déjà comptabilisés, à partir de*

Une case à cocher permet d'indiquer si des bulletins déjà comptabilisés, doivent faire l'objet d'une nouvelle comptabilisation. Ces bulletins seront ceux compris entre la date indiquée ici, jusqu'à la date indiquée précédemment **Comptabilisation au**.

#### *Edition du journal de Paie*

Cette édition reprend tous les éléments transférés en comptabilité sur la période sélectionnée.

#### *Date de la passation / Référence / Libellé*

La date de passation par défaut est celle du dernier jour du mois en cours, la conserver ou la modifier.

Le programme propose comme référence PAIE suivie du mois et de l'année en cours, et comme libellé OD PAIE. Conservez ou modifiez ces deux propositions par défaut.

Le programme affiche les référence et libellé pour toutes les lignes d'écritures ne possédant pas de référence et libellé.

#### *Type d'écriture*

Sélectionnez 'Normal' pour éditer le journal de Paie.

### Sélection du format d'impression

![](_page_39_Figure_12.jpeg)

## Emplacement des fichiers PDF

Après sélection du répertoire *Paie 2006*, modifiez le nom du fichier en indiquant la période concernée par la mise à jour comptable des écritures.

#### *Exemple :*

*Journal\_Comptable\_Paie\_010206\_280206.pdf* 

![](_page_40_Figure_5.jpeg)

## Paie pour Macintosh

Avant la clôture annuelle de la comptabilité veuillez lancer la fonction *Journaux comptables* du menu *Etat*, la fenêtre suivante est proposée :

![](_page_41_Picture_3.jpeg)

La fenêtre de sélection du journal comptable se présente comme suit :

Les réglages par défaut offerts par cette fenêtre permettent d'obtenir un état donnant les écritures comptables de paie sur la période sélectionnée.

#### *Etablissement*

Laissez l'option par défaut : **Tous** 

#### *Période*

Zones de saisie permettant d'enregistrer la période sur laquelle vous souhaitez obtenir l'impression du journal. La période doit correspondre à celle de vos écritures de paie.

Ces zones comportent un bouton permettant d'ouvrir un calendrier et de sélectionner facilement une date.

## *Type*

- **Les deux** : (valeur par défaut) sont imprimées les écritures comptables de salaires et de charges ;
- **Salaires** : ne sont imprimées que les écritures comptables des salaires bruts et des cotisations salariales
- **Charges** : ne sont imprimées que les écritures comptables des cotisations patronales.

Sélectionner l'option correspondant à votre mode de gestion.

#### *Détail par salarié*

La liste déroulante permet de choisir entre :

- **Net à payer** : le net à payer est réparti sur le compte salarié défini dans chaque volet **Structure / Salariés / Qualification** de la fiche salarié (la rubrique **Net à payer** est définie dans le volet **A propos de… / Préférences**).
- **Acompte** : l'acompte est réparti sur le compte salarié défini dans chaque fiche salarié (la rubrique **Acompte** est définie dans le volet **Préférences** de la présente commande).
- **Les deux** : le net à payer et l'acompte sont répartis sur les comptes définis dans chaque fiche salarié.
- **Aucun** : (valeur par défaut) la mise à jour en comptabilité est effectuée sans les détails par salarié.

Les choix **Net à payer**, **Acompte** et **Les deux** font générer autant de lignes d'écriture qu'il y a de salariés.

Le choix **Aucun** permet de regrouper les valeurs du net à payer et des acomptes en une seule écriture. Pour cela, vous devez définir au préalable le compte dans la zone *Compte net à payer* de ce volet. Sélectionner l'option correspondant à votre mode de gestion.

#### *Détail des rubriques*

Décochez cette option et cliquez sur le bouton [OK].

## Sélection du format d'impression

![](_page_42_Figure_12.jpeg)

## Emplacement des fichiers PDF

Après sélection du répertoire *Paie 2006* modifiez le nom de fichier en indiquant la période concernée par la mise à jour comptable des écritures:

#### *Exemple :*

*Journal\_comptable\_Paie\_010106\_310306.pdf.* 

Vérifiez la concordance des informations avec la comptabilité.

Cette opération doit être répétée autant de fois que la fréquence des mises à jour comptable.

## Intangibilité des pièces commerciales

**Paragraphes 30 à 48 de l'instruction – Principe de permanence du chemin de révision** 

Î **Processus de comptabilisation des pièces commerciales** 

**Le texte mentionne l'obligation de permanence du chemin de révision c'est à dire l'intangibilité entre notamment la pièce commerciale justificative et l'écriture comptable correspondante. Par extension ce principe peut être étendu aux autres applications Immobilisations, Moyens de paiement, Paie et Etats comptables et fiscaux.** 

## Gestion commerciale, Start Compta facture, Saisie de caisse décentralisée

Après chaque mise à jour comptable des applications citées il est nécessaire de procéder à la clôture de ces écritures dans la comptabilité :

Lancez la fonction de clôture d'exercice de votre application Sage Comptabilité

Menu *Traitement*, *Clôture de journaux*, l'assistant de clôture est proposé :

![](_page_45_Figure_5.jpeg)

Sélectionnez l'option « Partielle » puis cliquez sur le bouton suivant

#### Sélection du journal de vente

![](_page_46_Figure_2.jpeg)

![](_page_46_Picture_3.jpeg)

*Le processus de clôture du journal de vente décrite ci-dessous doit également être appliqué en cas d'utilisation d'un logiciel de facturation externe quel que soit le processus de mise à jour comptable utilisé, importation, utilisation d'un lien ODBC, écritures en direct ou par exploitation des objets métiers Sage dans une base relationnelle.* 

Sélectionner par un simple clic les journaux à clôturer partiellement. La suppression ou modification des éléments comptables (Date, N° compte, Montant) n'est plus autorisée. Il est cependant possible d'ajouter de nouvelles écritures comme par exemple de nouvelles ventes ou règlements à partir de la gestion commerciale.

#### *Sélectionner la date de validation des écritures.*

Par défaut, la date du jour est proposée. Nous vous conseillons d'indiquer la même date des pièces commerciales mises à jour.

L'impression des journaux n'est pas obligatoire à cette étape, vous pouvez sélectionner l'option Non.

Cliquez sur le bouton **Fin** pour lancer le traitement.

# Archivage dans les applications périphériques

Nous vous conseillons d'archiver également les journaux comptables émis à partir de ces différentes applications ainsi que les factures de ventes émises par la Gestion commerciale ou Saisie de caisse décentralisée.

Vous trouverez ci-dessous la description de ce processus pour l'ensemble des applications concernées.

Veuillez procéder à la sauvegarde du fichier \*.pdf généré dans les processus décris ci-dessous afin de le conserver en archive sur un support pérenne de votre choix (exemple CD ou DVD non réinscriptibles…).

**« Les entreprises doivent conserver les livres, registres, documents […] sous une forme dématérialisée dans un format immédiatement lisible. »** 

**Le délai général de conservation est de 6 ans et de 3 ans minimum sur support informatique**

![](_page_47_Picture_7.jpeg)

*Vous pouvez bien entendu imprimer le fichier pdf afin de conserver une archive papier* 

## Gestion commerciale, Start Compta facture, Saisie de caisse décentralisée

#### Impression des journaux

Veuillez procéder avant à la clôture annuelle de la comptabilité à l'impression des journaux à partir de la gestion commerciale. Ceci permettra ainsi de justifier en comptabilité l'origine des mouvements de la gestion commerciale. Nous vous invitons également vivement à comparer les totaux des journaux de vente ainsi imprimés avec ceux de la comptabilité.

Lancez la fonction *Journaux comptables* du menu *Etat*, la fenêtre suivante est proposée :

![](_page_48_Picture_5.jpeg)

#### *Domaine :*

Liste déroulante permettant la sélection des états comptables :

- **Factures des ventes** : (valeur par défaut) permet l'impression des états relatifs au journal des ventes.
- **Factures des achats** : permet l'impression des états relatifs au journal des achats.
- **Règlements clients** : permet l'impression des états relatifs au journal des règlements des ventes.
- **Règlements fournisseurs** : permet l'impression des états relatifs au journal des règlements des achats.

Sélectionnez le domaine en fonction de votre gestion. Attention ! L'opération d'impression et de conservation des journaux comptables correspondant doit être répétée pour chacun des domaines.

#### *Journal analytique*

Liste déroulante permettant d'imprimer le journal analytique correspondant au plan désigné en ventilation. Sélectionner l'option appropriée.

#### *Etat des pièces*

Liste déroulante permettant de prendre en compte, lors des impressions, soit les pièces comptabilisées, soit les pièces non comptabilisées. Sélectionnez l'option par défaut « pièces comptabilisées »

#### *Date de / à*

Zones permettant de sélectionner la période à prendre en compte pour l'impression. Par défaut, le programme reprend l'année civile correspondant à la date du micro-ordinateur. Veuillez sélectionnez la période correspondante à votre exercice comptable

Ces zones comportent un bouton permettant d'ouvrir un calendrier et de sélectionner facilement une date.

Cliquez sur le bouton [OK]

#### Sélection du format d'impression

![](_page_49_Figure_10.jpeg)

*Cochez impérativement l'option « Impression dans un fichier PDF » et cliquez sur le bouton [OK].* 

La tenue d'une comptabilité informatisée est soumise à des obligations en termes de conservation et de présentation des documents comptables, récapitulées dans l'instruction de la Direction Générale des Impôts n° 13 L-1-06 en date du 24 janvier 2006, obligations que chaque Utilisateur se doit de respecter. La fenêtre Impression permet d'imprimer les documents au format PDF. Il incombe à l'utilisateur de les archiver et de les conserver sur un support pérenne et ainsi de respecter ces obligations.

#### *Equivalent sur Macintosh*

![](_page_50_Figure_3.jpeg)

#### Emplacement des fichiers PDF

![](_page_50_Figure_5.jpeg)

Après sélection du répertoire *Documents gestion commerciale 2006*, modifiez le nom de fichier en indiquant la période concernée par la clôture:

#### *Exemple :*

*Journaux\_ventes\_gescom\_2006.pdf* 

Répétez l'opération pour chaque domaine géré.

#### Impression des factures

Liste des documents des ventes : On peut ouvrir cette commande en cliquant sur le bouton Liste des documents de vente de la barre d'outils «Gestion des ventes».

On peut aussi ouvrir la liste des documents de vente en cliquant sur l'icône Liste des documents de vente de la barre verticale «Gestion des ventes».

On peut également y accéder à partir du menu Traitement, Documents des ventes

![](_page_51_Picture_9.jpeg)

#### *Bouton Sélectionner les documents*

Ouvre la fenêtre permettant d'effectuer des sélections dans la liste

![](_page_52_Picture_3.jpeg)

#### *Période de / à*

Indiquez la période correspondante à votre exercice comptable. Cette période peut-être réduite au trimestre, au mois… en fonction du volume de factures gérées afin de faciliter la recherche des documents.

#### *Liste déroulante Document*

Sélectionnez l'option : **Facture comptabilisée** : seules les factures comptabilisées apparaissent.

#### *Sélection des documents*

Veuillez sélectionner l'ensemble des factures, vous pouvez utiliser à cet effet le menu contextuel, Sélectionnez tout à l'aide du clic droit de la souris ou le raccourci clavier Ctrl + A.

#### *Bouton [Imprimer le(s) document(s)*

Ce bouton, disposé sur le bord inférieur de la liste des documents de vente, lance l'impression des documents. Cliquez ensuite sur ce bouton. Selon que vous avez défini ou non un modèle par défaut la fenêtre suivante vous permet de sélectionner un modèle de mise en page.

![](_page_53_Figure_1.jpeg)

#### Sélection du format d'impression

![](_page_53_Figure_3.jpeg)

![](_page_54_Picture_1.jpeg)

*Cochez impérativement l'option « Impression dans un fichier PDF » et cliquez sur le bouton [OK].* 

La tenue d'une comptabilité informatisée est soumise à des obligations en termes de conservation et de présentation des documents comptables, récapitulées dans l'instruction de la Direction Générale des Impôts n° 13 L-1-06 en date du 24 janvier 2006, obligations que chaque Utilisateur se doit de respecter. La fenêtre Impression permet d'imprimer les documents au format PDF. Il incombe à l'utilisateur de les archiver et de les conserver sur un support pérenne et ainsi de respecter ces obligations.

#### *Equivalent sur Macintosh*

![](_page_54_Figure_5.jpeg)

#### Emplacement des fichiers PDF

![](_page_54_Figure_7.jpeg)

Après sélection du répertoire *Documents gestion commerciale 2006*, modifiez le nom de fichier en indiquant la période concernée par la clôture, l'exercice comptable, le trimestre, le mois… en fonction du volume de facture géré :

#### *Exemple :*

Factures\_ventes\_gescom\_010106\_311206.pdf

## Moyens de paiement

Veuillez procéder avant à la clôture annuelle de la comptabilité à l'impression des journaux à partir de Moyens de Paiement.

Lancez la fonction *Mise à jour de la comptabilité* du menu *Traitement*. La fenêtre suivante est proposée :

![](_page_56_Picture_4.jpeg)

Sélectionner l'option Edition du journal comptable.

#### *Date limite*

Indiquez la date de fin d'exercice.

#### *Etat des échéances*

Liste déroulante permettant de prendre en compte, lors des impressions, soit les pièces comptabilisées, soit les pièces non comptabilisées. Sélectionnez l'option « pièces comptabilisées »

Cliquez sur le bouton [Mise à jour directe]

#### Sélection du format d'impression

![](_page_57_Figure_2.jpeg)

![](_page_57_Picture_3.jpeg)

Cochez impérativement l'option *Impression dans un fichier PDF* et cliquez sur le bouton [OK].

La tenue d'une comptabilité informatisée est soumise à des obligations en termes de conservation et de présentation des documents comptables, récapitulées dans l'instruction de la Direction Générale des Impôts n° 13 L-1-06 en date du 24 janvier 2006, obligations que chaque Utilisateur se doit de respecter. La fenêtre Impression permet d'imprimer les documents au format PDF. Il incombe à l'utilisateur de les archiver et de les conserver sur un support pérenne et ainsi de respecter ces obligations.

#### *Equivalent sur Macintosh*

![](_page_58_Figure_2.jpeg)

### Emplacement des fichiers PDF

![](_page_58_Figure_4.jpeg)

Après sélection du répertoire *Moyens de paiement 2006* modifiez le nom de fichier en indiquant la période concernée par la clôture:

#### *Exemple :*

*Journaux\_comptables\_MDP\_010106\_311206.pdf.* 

## Immobilisations

Veuillez procéder avant à la clôture annuelle de la comptabilité l'impression des journaux de à partir des Immobilisations.

Lancez la fonction *Mise à jour comptable* du menu *Traitement.* La fenêtre suivante est proposée*.* 

![](_page_59_Picture_4.jpeg)

#### *Type*

Liste déroulante permettant de choisir entre :

- Exercice **:** comptabilisation annuelle des écritures en date de fin d'exercice,
- Mois : comptabilisation mensuelle avec régularisation éventuelle sur le dernier mois de l'exercice,
- Situation : impression du journal comptable à une date différente de celle de la fin d'exercice. Les valeurs obtenues seront calculées en fonction de la date de situation saisie dans les listes déroulante

#### *Période.*

Sélectionner l'option conformément à la fréquence de mise à jour des écritures, mensuelle, annuelle. Si vous comptabiliser vos écritures avec une fréquence différente (ex : mise à jour trimestrielle) veuillez sélectionner l'option « Situation ».

#### *Exercice*

Liste déroulante permettant de sélectionner l'exercice sur lequel portera l'impression. Par défaut, le dernier exercice sur lequel un calcul des amortissements (fonction *Traitement / Calcul des amortissements*) a été lancé est proposé.

#### *Période de / à*

Dans le cadre de l'impression d'un journal de type Mois ou Situation, saisissez dans les colonnes *De*  et *à* les dates de la situation demandée.

#### *Ecritures*

Sélectionnez la valeur **« Tout ».**

Cliquez sur le bouton [OK]

#### Sélection du format d'impression

![](_page_60_Picture_7.jpeg)

![](_page_60_Picture_8.jpeg)

*Cochez impérativement l'option* **Impression dans un fichier PDF** *et cliquez sur le bouton [OK].* 

La tenue d'une comptabilité informatisée est soumise à des obligations en termes de conservation et de présentation des documents comptables, récapitulées dans l'instruction de la Direction Générale des Impôts n° 13 L-1-06 en date du 24 janvier 2006, obligations que chaque Utilisateur se doit de respecter. La fenêtre Impression permet d'imprimer les documents au format PDF. Il incombe à

l'utilisateur de les archiver et de les conserver sur un support pérenne et ainsi de respecter ces obligations.

#### *Equivalent sur Macintosh*

![](_page_61_Figure_3.jpeg)

## Emplacement des fichiers PDF

![](_page_61_Figure_5.jpeg)

Après sélection du répertoire *Immobilisations 2006* modifiez le nom de fichier en indiquant la période concernée par la clôture:

#### *Exemple :*

*Journaux\_comptables\_Immo\_011006\_311206.pdf.* 

Autres états des immobilisations à archiver au titre de l'exercice :

- Etat des immobilisations
- Etat des amortissements
- Etat des sorties
- Etat des crédit-bail / location

## Etats comptables et fiscaux

Veuillez procéder avant à la clôture annuelle de la comptabilité l'impression des journaux de à partir des Etats comptables et fiscaux si vous avez saisi des OD.

Lancez la fonction Journaux du menu Etats.

#### Sélection du format d'impression

![](_page_63_Picture_5.jpeg)

![](_page_63_Picture_6.jpeg)

*Cochez impérativement l'option* **Impression dans un fichier PDF** *et cliquez sur le bouton [OK].* 

La tenue d'une comptabilité informatisée est soumise à des obligations en termes de conservation et de présentation des documents comptables, récapitulées dans l'instruction de la Direction Générale des Impôts n° 13 L-1-06 en date du 24 janvier 2006, obligations que chaque Utilisateur se doit de respecter. La fenêtre Impression permet d'imprimer les documents au format PDF. Il incombe à l'utilisateur de les archiver et de les conserver sur un support pérenne et ainsi de respecter ces obligations.

#### Emplacement des fichiers PDF

![](_page_64_Figure_2.jpeg)

Après sélection du répertoire *Etats comptables et fiscaux 2006* modifiez le nom de fichier en indiquant la période concernée par la clôture:

#### *Exemple :*

*Journal\_ECF\_OD\_2006.pdf* 

# Chronologie des écritures en comptabilité

Afin d'assurer la chronologie des écritures comptables il est nécessaire d'utiliser les options de numérotation continue et de protection du numéro de pièce.

Lancez la fonction A propos de votre application Sage Comptabilité,

Menu *Fichier*, volet *Paramètres*, la fenêtre suivante est proposée :

![](_page_65_Figure_5.jpeg)

Dans le sous volet *Saisie*, cochez les options :

- Protection de la zone N° pièce
- Numérotation continue pour le fichier

A la génération du message d'alerte ci-dessous cliquez sur le bouton [OUI]

![](_page_66_Picture_1.jpeg)

![](_page_66_Picture_2.jpeg)

*Vous disposez des zones Référence et N° facture pour identifier vos factures.* 

L'activation du paramétrage vous permettant d'utiliser les options de numérotation continue et de protection du numéro de pièce est nécessaire pour que la tenue de votre comptabilité informatisée respecte les principes du caractère intangible ou de l'irréversibilité des écritures comptables, d'une clôture périodique des enregistrements chronologiques et de la permanence du chemin de révision.

Ainsi il est de la responsabilité de l'Utilisateur d'activer ce paramétrage.

En cas de contrôle fiscal, Sage ne pourrait pas être tenue responsable de la non activation du paramétrage permettant aux Utilisateurs d'utiliser les options de numérotation continue et de protection du numéro de pièce.

## Documentations des logiciels

#### Paragraphe 49 à 56 : ces points traitent de la documentation fournie avec les logiciels

**Les logiciels Sage sont livrés avec leur manuel de référence correspondant. Les manuels intègrent la description détaillée de l'ensemble des fonctionnalités de l'application ainsi que l'indication des évolutions significatives propres à chaque version. Les manuels de références sont complétés du manuel de la gamme qui décrit l'ensemble des fonctionnalités communes, d'un manuel d'installation et d'un manuel spécifique pour les bases relationnelles.**

Paragraphe 57. La loi n° 94-361 du 10 mai 1994 prévoit un accès très restrictif au code source des programmes

Développés par des concepteurs indépendants de l'entreprise vérifiée.

**Afin de répondre à cette exigence Sage est adhérent de l'Agence pour la Protection des Programmes (APP) auprès de qui elle dépose régulièrement les programmes sources et leurs différentes mises à jour.**