import os

def create_project_structure(base_dir="MixMentorAI"):
    folders = [
        f"{base_dir}/backend/app/routes",
        f"{base_dir}/backend/app/models",
        f"{base_dir}/backend/app/crud",
        f"{base_dir}/backend/app/tests",
        f"{base_dir}/backend/alembic/versions",
        f"{base_dir}/frontend/electron/renderer",
        f"{base_dir}/frontend/react/src/components",
        f"{base_dir}/frontend/react/src/pages",
        f"{base_dir}/frontend/react/public",
        f"{base_dir}/frontend/overlay",
        f"{base_dir}/ocr_module",
        f"{base_dir}/plugin_scanner",
        f"{base_dir}/ai_recommender",
        f"{base_dir}/cloud_sync",
        f"{base_dir}/scripts",
    ]

    files = [
        f"{base_dir}/backend/app/__init__.py",
        f"{base_dir}/backend/app/main.py",
        f"{base_dir}/backend/app/config.py",
        f"{base_dir}/backend/app/dependencies.py",
        f"{base_dir}/backend/app/routes/__init__.py",
        f"{base_dir}/backend/app/routes/auth.py",
        f"{base_dir}/backend/app/routes/projects.py",
        f"{base_dir}/backend/app/routes/plugins.py",
        f"{base_dir}/backend/app/routes/payments.py",
        f"{base_dir}/backend/app/models/__init__.py",
        f"{base_dir}/backend/app/models/user.py",
        f"{base_dir}/backend/app/models/project.py",
        f"{base_dir}/backend/app/models/plugin.py",
        f"{base_dir}/backend/app/crud/__init__.py",
        f"{base_dir}/backend/app/crud/user.py",
        f"{base_dir}/backend/app/crud/project.py",
        f"{base_dir}/backend/app/crud/plugin.py",
        f"{base_dir}/backend/app/tests/test_auth.py",
        f"{base_dir}/backend/app/tests/test_projects.py",
        f"{base_dir}/backend/app/tests/test_plugins.py",
        f"{base_dir}/backend/requirements.txt",
        f"{base_dir}/backend/.env.example",
        f"{base_dir}/backend/alembic/env.py",
        f"{base_dir}/frontend/electron/main.js",
        f"{base_dir}/frontend/electron/preload.js",
        f"{base_dir}/frontend/electron/renderer/index.html",
        f"{base_dir}/frontend/electron/renderer/app.js",
        f"{base_dir}/frontend/electron/renderer/styles.css",
        f"{base_dir}/frontend/react/src/App.js",
        f"{base_dir}/frontend/react/src/index.js",
        f"{base_dir}/frontend/react/package.json",
        f"{base_dir}/frontend/overlay/overlay.py",
        f"{base_dir}/frontend/overlay/utils.py",
        f"{base_dir}/ocr_module/ocr_handler.py",
        f"{base_dir}/ocr_module/yolo_pipeline.py",
        f"{base_dir}/ocr_module/screenshot.py",
        f"{base_dir}/ocr_module/preprocessing.py",
        f"{base_dir}/plugin_scanner/scanner.py",
        f"{base_dir}/plugin_scanner/metadata_parser.py",
        f"{base_dir}/plugin_scanner/local_db.py",
        f"{base_dir}/ai_recommender/recommender.py",
        f"{base_dir}/ai_recommender/embeddings.py",
        f"{base_dir}/ai_recommender/model_pipeline.py",
        f"{base_dir}/cloud_sync/supabase.py",
        f"{base_dir}/cloud_sync/firebase.py",
        f"{base_dir}/cloud_sync/migration.py",
        f"{base_dir}/scripts/deploy.sh",
        f"{base_dir}/scripts/setup_dev.sh",
        f"{base_dir}/scripts/seed_db.py",
        f"{base_dir}/.gitignore",
        f"{base_dir}/README.md",
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    for file in files:
        with open(file, "w") as f:
            f.write("")  # Create empty files

    print(f"Project structure created under '{base_dir}'.")

if __name__ == "__main__":
    create_project_structure()