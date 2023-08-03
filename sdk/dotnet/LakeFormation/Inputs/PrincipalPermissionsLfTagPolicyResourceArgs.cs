// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.LakeFormation.Inputs
{

    public sealed class PrincipalPermissionsLfTagPolicyResourceArgs : global::Pulumi.ResourceArgs
    {
        [Input("catalogId", required: true)]
        public Input<string> CatalogId { get; set; } = null!;

        [Input("expression", required: true)]
        private InputList<Inputs.PrincipalPermissionsLfTagArgs>? _expression;
        public InputList<Inputs.PrincipalPermissionsLfTagArgs> Expression
        {
            get => _expression ?? (_expression = new InputList<Inputs.PrincipalPermissionsLfTagArgs>());
            set => _expression = value;
        }

        [Input("resourceType", required: true)]
        public Input<Pulumi.AwsNative.LakeFormation.PrincipalPermissionsResourceType> ResourceType { get; set; } = null!;

        public PrincipalPermissionsLfTagPolicyResourceArgs()
        {
        }
        public static new PrincipalPermissionsLfTagPolicyResourceArgs Empty => new PrincipalPermissionsLfTagPolicyResourceArgs();
    }
}
