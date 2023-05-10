{ pkgs ? import <nixpkgs> {} }:

pkgs.python3.withPackages (ps: with ps; [
  pkgs.virtualenv
]) .override (oldAttrs: {
  preBuild = ''
    virtualenv --no-download $out
    source $out/bin/activate
    pip install -r $src/requirements.txt
  '';
})
