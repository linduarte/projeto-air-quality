import dearpygui.dearpygui as dpg
import numpy as np
import utils  # Seu motor de auditoria e limpeza
import os

# CAMINHO DO SEU ARQUIVO ORIGINAL (RAW)
CSV_PATH = r"data/raw/pollution_data.csv"
OUTPUT_PATH = r"data/processed/clean_data.csv"

df, status = utils.load_and_audit_pollution_data(CSV_PATH)

def load_data():
    global df, status
    df, status = utils.load_and_audit_pollution_data(CSV_PATH)

def get_plot_data(area_type):
    if df is None:
        return [], []
    # No seu CSV, verifique se 'Industrial' e 'Residential' começam com maiúscula
    mask = df['Type'] == area_type 
    filtered = df[mask].sort_values('Date')
    
    if filtered.empty:
        return [], []

    x = filtered['Date'].values.astype(np.int64) // 10**9
    y = filtered['PM2.5'].values
    return list(x), list(y)

dpg.create_context()

with dpg.window(label="Monitor Ambiental - Dashboard", width=1000, height=750):
    dpg.add_text("Análise de Poluição: PM2.5", color=[0, 255, 255])
    dpg.add_text(f"Status: {status}", tag="status_text")
    
    dpg.add_separator()

    with dpg.plot(label="Tendência PM2.5", height=450, width=-1, query=True):
        dpg.add_plot_legend()
    
    # Eixos
        x_axis = dpg.add_plot_axis(dpg.mvXAxis, label="Tempo (Use Scroll para Zoom)")
        y_axis = dpg.add_plot_axis(dpg.mvYAxis, label="µg/m³")

        # Ferramenta de Precisão (Crosshair)
        # Mostra uma linha vertical e horizontal que segue o mouse
        dpg.add_plot_annotation(label="Cursor de Análise", default_value=(0, 0), tag="cursor_info")

        if df is not None:
            # Tenta carregar as duas zonas
            x_ind, y_ind = get_plot_data('Industrial')
            if x_ind:
                dpg.add_line_series(x_ind, y_ind, label="Industrial", parent=y_axis)
                # O Tooltip da série Industrial entra aqui:
                with dpg.tooltip(dpg.last_item()):
                    dpg.add_text("Zona Industrial: Concentração de PM2.5")

            x_res, y_res = get_plot_data('Residential')
            if x_res:
                dpg.add_line_series(x_res, y_res, label="Residencial", parent=y_axis)
                # O Tooltip da série Residencial entra aqui:
                with dpg.tooltip(dpg.last_item()):
                    dpg.add_text("Zona Residencial: Concentração de PM2.5")

    dpg.add_separator()
    
    def export_data():
        if df is not None:
            os.makedirs("data/processed", exist_ok=True)
            df.to_csv(OUTPUT_PATH, index=False)
            dpg.set_value("status_text", f"✅ Exportado para: {OUTPUT_PATH}")

    dpg.add_button(label="Gerar Arquivo Processado (Clean Data)", callback=export_data)

dpg.create_viewport(title='Air Quality Lab', width=1050, height=800)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()