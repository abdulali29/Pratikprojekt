# Pratikprojekt








Under udviklingen blev en Azure access key utilsigtet inkluderet i versionsstyringen. GitHub’s push protection identificerede dette og blokerede push’et. Problemet blev løst ved at fjerne committen fra historikken og anvende environment variables via en .env-fil. Dette sikrer korrekt håndtering af følsomme oplysninger i systemet.
