// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SSM.Inputs
{

    public sealed class PatchBaselineRuleGroupArgs : Pulumi.ResourceArgs
    {
        [Input("patchRules")]
        private InputList<Inputs.PatchBaselineRuleArgs>? _patchRules;
        public InputList<Inputs.PatchBaselineRuleArgs> PatchRules
        {
            get => _patchRules ?? (_patchRules = new InputList<Inputs.PatchBaselineRuleArgs>());
            set => _patchRules = value;
        }

        public PatchBaselineRuleGroupArgs()
        {
        }
    }
}
