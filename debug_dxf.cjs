const fs = require('fs');
const { DxfParser } = require('dxf-parser');

async function debug() {
    try {
        const fileContent = fs.readFileSync('c:\\Users\\Tomek\\Desktop\\AstroStuff\\Scorpio\\sample.dxf', 'utf-8');
        const parser = new DxfParser();
        const dxf = parser.parseSync(fileContent);

        console.log("Entities found:", dxf.entities.length);
        dxf.entities.forEach((e, i) => {
            console.log(`\nEntity ${i} (${e.type}):`);
            if (e.type === 'LINE') {
                console.log("  Vertices:", JSON.stringify(e.vertices));
            } else if (e.type === 'ARC') {
                console.log("  Center:", JSON.stringify(e.center));
                console.log("  Radius:", e.radius);
                console.log("  Angles:", e.startAngle, e.endAngle);
            } else {
                console.log("  Data:", JSON.stringify(e));
            }
        });
    } catch (err) {
        console.error("Error:", err);
    }
}

debug();
