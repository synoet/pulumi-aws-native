// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AmplifyUIBuilder.Inputs
{

    public sealed class FormStyleConfig0PropertiesArgs : global::Pulumi.ResourceArgs
    {
        [Input("tokenReference", required: true)]
        public Input<string> TokenReference { get; set; } = null!;

        public FormStyleConfig0PropertiesArgs()
        {
        }
        public static new FormStyleConfig0PropertiesArgs Empty => new FormStyleConfig0PropertiesArgs();
    }
}
