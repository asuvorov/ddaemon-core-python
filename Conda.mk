.DEFAULT_GOAL := help

ENV_NAME := core
PY_VERSION := "3.10"

# =============================================================================
# === (mini)Conda Targets.
# =============================================================================
##@ Conda
create: ## Create Conda Environment.
	$(info Creating Conda Environment)
	@conda env create -f environment.yml
.PHONY: create

update: ## Update Conda Environment.
	$(info Updating Conda Environment)
	@conda env update --file environment.yml --prune
.PHONY: update

clone: ## Create an identical Environment on the same or another Machine.
	$(info Creating an identical Environment)
	@conda create --name $(ENV_NAME) --file spec-file.txt
.PHONY: clone

# install: ## Install listed Packages into an existing Environment.
# 	$(info Installing Conda Environment Packages)
# 	@conda install --name $(ENV_NAME) --file spec-file.txt
# .PHONY: install

activate: ## Activate Conda Environment.
	$(info Activating Conda Environment)
	@conda activate $(ENV_NAME)
.PHONY: activate

export: ## Export Conda Environment.
	$(info Exporting Conda Environment)
	@conda env export > environment.yml
	@conda list --explicit > spec-file.txt
.PHONY: export

remove: ## Remove Conda Environment.
	$(info Removing Conda Environment)
	@conda deactivate
	@conda remove --name $(ENV_NAME) --all
.PHONY: remove
