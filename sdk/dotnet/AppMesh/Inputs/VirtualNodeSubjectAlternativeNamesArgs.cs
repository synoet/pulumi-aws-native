// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppMesh.Inputs
{

    public sealed class VirtualNodeSubjectAlternativeNamesArgs : global::Pulumi.ResourceArgs
    {
        [Input("match", required: true)]
        public Input<Inputs.VirtualNodeSubjectAlternativeNameMatchersArgs> Match { get; set; } = null!;

        public VirtualNodeSubjectAlternativeNamesArgs()
        {
        }
        public static new VirtualNodeSubjectAlternativeNamesArgs Empty => new VirtualNodeSubjectAlternativeNamesArgs();
    }
}
