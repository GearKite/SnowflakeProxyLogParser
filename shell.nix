# Template
with import <nixpkgs> { };

mkShell {

  nativeBuildInputs = [
    direnv
    python312
    python312Packages.plotly
    python312Packages.pandas
    python312Packages.packaging
  ];

  NIX_ENFORCE_PURITY = true;

  shellHook = ''
  '';
}
