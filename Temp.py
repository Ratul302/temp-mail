import base64
exec(base64.b64decode("IyB1c2UgcHl0aG9uMyB5YSBicm8NCiMgTGlhdCBhcGEgYW5qaW5nID46KA0KdHJ5Og0KCWltcG9ydCByZXF1ZXN0cyBhcyByLCByYW5kb20sIGpzb24sIG9zDQoJZnJvbSB0aW1lIGltcG9ydCBzbGVlcA0KZXhjZXB0IE1vZHVsZU5vdEZvdW5kRXJyb3I6DQoJZXhpdCgiWyFdIE1vZHVsZSBub3QgaW5zdGFsbGVkIikNCg0KbGlzdF9tYWlsID0gWyJ2aW50b21hcGVyLmNvbSIsInRvdmluaXQuY29tIiwibWVudG9uaXQubmV0Il0NCnVybCA9ICJodHRwczovL2NyeXB0b2dtYWlsLmNvbS8iDQpudW0gPSAwDQoNCmRlZiBnZXRfdGVrcyhhY2NlcHQsIGtleSk6DQoJY2VrID0gci5nZXQodXJsKyJhcGkvZW1haWxzLyIra2V5LCBoZWFkZXJzPXsiYWNjZXB0IjogYWNjZXB0fSkudGV4dA0KCWlmICJlcnJvciIgaW4gY2VrOg0KCQlyZXR1cm4gIi0iDQoJZWxzZToNCgkJcmV0dXJuIGNlay5zdHJpcCgpDQoNCmRlZiBnZXRfcmFuZG9tKGRpZ2l0KToNCglsaXMgPSBsaXN0KCJhYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5ejAxMjM0NTY3ODkiKQ0KCWRpZyA9IFtyYW5kb20uY2hvaWNlKGxpcykgZm9yIF8gaW4gcmFuZ2UoZGlnaXQpXQ0KCXJldHVybiAiIi5qb2luKGRpZyksIHJhbmRvbS5jaG9pY2UobGlzdF9tYWlsKQ0KDQpkZWYgYW5pbWF0ZSh0ZWtzKToNCglsaXMgPSBsaXN0KCJcfC8tIikNCglmb3IgY3kgaW4gbGlzOg0KCQlwcmludCgiXHJbIitjeSsiXSAiK3N0cih0ZWtzKSsiLi4gIiwgZW5kPSIiKQ0KCQlzbGVlcCgwLjUpDQoNCmRlZiBydW4oZW1haWwpOg0KCXdoaWxlIFRydWU6DQoJCXRyeToNCgkJCWFuaW1hdGUoIldhaXRpbmcgZm9yIGluY29taW5nIG1lc3NhZ2UiKQ0KCQkJcmF1biA9IHIuZ2V0KHVybCsiYXBpL2VtYWlscz9pbmJveD0iK2VtYWlsKS50ZXh0DQoJCQlpZiAiNDA0IiBpbiByYXVuOg0KCQkJCWNvbnRpbnVlDQoJCQllbGlmICJkYXRhIiBpbiByYXVuOg0KCQkJCXogPSBqc29uLmxvYWRzKHJhdW4pDQoJCQkJZm9yIGRhdGEgaW4gelsiZGF0YSJdOg0KCQkJCQlwcmludCgiXHJb4oCiXSBJRDogIitkYXRhWyJpZCJdLCBlbmQ9IlxuIikNCgkJCQkJZ290ID0ganNvbi5sb2FkcyhyLmdldCh1cmwrImFwaS9lbWFpbHMvIitkYXRhWyJpZCJdKS50ZXh0KQ0KCQkJCQlwZW5naXJpbSA9IGdvdFsiZGF0YSJdWyJzZW5kZXIiXVsiZGlzcGxheV9uYW1lIl0NCgkJCQkJZW1haWxfcGUgPSBnb3RbImRhdGEiXVsic2VuZGVyIl1bImVtYWlsIl0NCgkJCQkJc3ViamVjdCAgPSBnb3RbImRhdGEiXVsic3ViamVjdCJdDQoJCQkJCXByaW50KCJcclvigKJdIFNlbmRlciBOYW1lOiAiK3BlbmdpcmltLCBlbmQ9IlxuIikNCgkJCQkJcHJpbnQoIlxyW+KAol0gU2VuZGVyIG1haWw6ICIrZW1haWxfcGUsIGVuZD0iXG4iKQ0KCQkJCQlwcmludCgiXHJb4oCiXSBTdWJqZWN0ICAgIDogIitzdWJqZWN0LCBlbmQ9IlxuIikNCgkJCQkJcHJpbnQoIlxyW+KAol0gTWVzc2FnZSAgICA6ICIrZ2V0X3Rla3MoInRleHQvaHRtbCx0ZXh0L3BsYWluIixkYXRhWyJpZCJdKSwgZW5kPSJcbiIpDQoJCQkJCWF0YyA9IGdvdFsiZGF0YSJdWyJhdHRhY2htZW50cyJdDQoJCQkJCWlmIGF0YyA9PSBbXToNCgkJCQkJCXByaW50KCJcclvigKJdIGF0dGFjaG1lbnRzOiAtIiwgZW5kPSJcbiIpDQoJCQkJCWVsc2U6DQoJCQkJCQlwcmludCgiW+KAol0gYXR0YWNobWVudHM6ICIpDQoJCQkJCQlmb3IgYXRjaCBpbiBhdGM6DQoJCQkJCQkJaWQgPSBhdGNoWyJpZCJdDQoJCQkJCQkJbmFtZSA9IGF0Y2hbImZpbGVfbmFtZSJdDQoJCQkJCQkJbmFtZSA9IG5hbWUuc3BsaXQoIi4iKVstMV0NCgkJCQkJCQlzdmVlID0gci5nZXQoImh0dHBzOi8vY3J5cHRvZ21haWwuY29tL2FwaS9lbWFpbHMvIitkYXRhWyJpZCJdKyIvYXR0YWNobWVudHMvIitpZCkNCgkJCQkJCQlvcGVuKGlkKyIuIituYW1lLCAid2IiKS53cml0ZShzdmVlLmNvbnRlbnQpDQoJCQkJCQkJcHJpbnQoIiAgICAgIH4gIitpZCsiLiIrbmFtZSkNCgkJCQkJcHJpbnQoIi0iKjQ1KQ0KCQkJCQlyLmRlbGV0ZSh1cmwrImFwaS9lbWFpbHMvIitkYXRhWyJpZCJdKQ0KCQkJCWNvbnRpbnVlDQoJCQllbHNlOg0KCQkJCWNvbnRpbnVlDQoJCWV4Y2VwdCAoS2V5Ym9hcmRJbnRlcnJ1cHQsRU9GRXJyb3IpOg0KCQkJCWV4aXQoIlxuW+Kck10gUHJvZ3JhbSBmaW5pc2hlZCwgZXhpdGluZy4uLlxuIikNCg0KZGVmIGNla191cGRhdGUodmVyc2lvbik6DQoJY2hlY2sgPSByLmdldCgiaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL2hla2VscHJvL3RlbXAtbWFpbC9tYWluL19fdmVyc2lvbl9fIikudGV4dC5zdHJpcCgpDQoJaWYgZmxvYXQodmVyc2lvbikgPCBmbG9hdChjaGVjayk6DQoJCXByaW50KCJb4pyTXSBVcGRhdGUgZm91bmQgLi5cbiIpDQoJCW9zLnN5c3RlbSgiZ2l0IHB1bGwiKQ0KCQltYWluKCkNCgllbHNlOg0KCQlwcmludCgiW8OXXSBVcGRhdGUgbm90IGZvdW5kLCBiYWNrIG1lbnUiKQ0KCQlzbGVlcCgyKQ0KCQltYWluKCkNCg0KZGVmIG1haW4oKToNCglvcy5zeXN0ZW0oJ2NsZWFyJykNCglnbG9iYWwgbnVtDQoJcHJpbnQoIiIiXDAzM1sxOzMybQ0KX19fX19fX19fX18gICAgICAgICAgICAgICAgICAgICAuX18uX18NClxfXyAgICBfX18vICAgICAgICBfX19fXyBfX19fXyAgfF9ffCAgfA0KICB8ICAgIHwgIF9fX19fXyAgLyAgICAgXFxcX18gIFwgfCAgfCAgfA0KICB8ICAgIHwgL19fX19fLyB8ICBZIFkgIFwvIF9fIFx8ICB8ICB8X18NCiAgfF9fX198ICAgICAgICAgfF9ffF98ICAoX19fXyAgL19ffF9fX18vDQogICAgICAgICAgICAgICAgICAgICAgIFwvICAgICBcLw0KDQogICAgKiBBdXRob3I6IFJhdHVsIEhhc2FuDQogICAgKiBHaXRodWI6IGh0dHBzOi8vZ2l0aHViLmNvbS9SYXR1bDMwMg0KICAgICogVGVhbSAgOiBEYXJrIEN5YmVyIEtpbmcgDQoNClswMV0gU0VUIEVNQUlMIFJBTkRPTQ0KWzAyXSBTRVQgRU1BSUwgQ1VTVE9NDQpbMDNdIENFSyBVUERBVEUNClswMF0gRVhJVA0KIiIiKQ0KDQoJcGlsID0gaW5wdXQoIls/XSBDaG9vc2U6ICIpDQoJd2hpbGUgcGlsID09ICIiIG9yIG5vdCBwaWwuaXNkaWdpdCgpOg0KCQlwaWwgPSBpbnB1dCgiWz9dIENob29zZTogIikNCglpZiBwaWwgaW4gWyIwMSIsIjEiXToNCgkJc2V0X25hbWUsIHNldF9lbWFpbCA9IGdldF9yYW5kb20oMTApDQoJCXByaW50KCJcblsqXSBZb3VyIGVtYWlsOiAiK3NldF9uYW1lKyJAIitzZXRfZW1haWwpDQoJCXByaW50KCJbKl0gQ1RSTCsgQyB0byBzdG9wcGVkLi4iKQ0KCQlwcmludCgiLSIqNDUpDQoJCXJ1bihzZXRfbmFtZSsiQCIrc2V0X2VtYWlsKQ0KCWVsaWYgcGlsIGluIFsiMDIiLCIyIl06DQoJCXNldF9uYW1lID0gaW5wdXQoIlvigKJdIFNldCBtYWlsIG5hbWU6ICIpDQoJCXByaW50KCkNCgkJZm9yIGN5IGluIGxpc3RfbWFpbDoNCgkJCW51bSArPSAxDQoJCQlwcmludCgiICIqNSwiWyIrc3RyKG51bSkrIl0gQCIrY3kpDQoJCXByaW50KCkNCgkJc2V0X2VtYWlsID0gaW5wdXQoIls/XSBTZWxlY3Q6ICIpDQoJCXdoaWxlIHNldF9lbWFpbCA9PSAiIiBvciBub3Qgc2V0X2VtYWlsLmlzZGlnaXQoKSBvciBpbnQoc2V0X2VtYWlsKSA+IGxlbihsaXN0X21haWwpOg0KCQkJc2V0X2VtYWlsID0gaW5wdXQoIls/XSBTZWxlY3Q6ICIpDQoJCW1haWwgPSBsaXN0X21haWxbaW50KHNldF9lbWFpbCktMV0NCgkJcHJpbnQoIlxuWypdIFlvdXIgZW1haWw6ICIrc2V0X25hbWUrIkAiK21haWwpDQoJCXByaW50KCJbKl0gQ1RSTCsgQyB0byBzdG9wcGVkLi4iKQ0KCQlwcmludCgiLSIqNDUpDQoJCXJ1bihzZXRfbmFtZSsiQCIrbWFpbCkNCgllbGlmIHBpbCBpbiBbIjAzIiwiMyJdOg0KCQl0cnk6DQoJCQl2ZXJzaSA9IG9wZW4oIl9fdmVyc2lvbl9fIiwiciIpLnJlYWQoKS5zdHJpcCgpDQoJCWV4Y2VwdDoNCgkJCXByaW50KCJbIV0gTm8gZnVydGhlciB1cGRhdGVzLi4iKQ0KCQkJc2xlZXAoMikNCgkJCW1haW4oKQ0KCQlwcmludCgiWyFdIFBsZWFzZSB3YWl0LCBjaGVjayB1cGRhdGUiKQ0KCQljZWtfdXBkYXRlKHZlcnNpKQ0KCWVsaWYgcGlsIGluIFsiMDAiLCIwIl06DQoJCWV4aXQoIls9XSBFeGl0IHByb2dyYW0sIGVuam95eVxuIikNCgllbHNlOg0KCQlleGl0KCJbLV0gTWVudSBub3QgZm91bmQsIGV4aXQuLlxuIikNCg0KDQppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOg0KCW1haW4oKQ0K"))
