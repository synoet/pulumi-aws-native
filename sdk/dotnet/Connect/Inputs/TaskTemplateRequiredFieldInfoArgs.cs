// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Connect.Inputs
{

    /// <summary>
    /// Required field info
    /// </summary>
    public sealed class TaskTemplateRequiredFieldInfoArgs : global::Pulumi.ResourceArgs
    {
        [Input("id", required: true)]
        public Input<Inputs.TaskTemplateFieldIdentifierArgs> Id { get; set; } = null!;

        public TaskTemplateRequiredFieldInfoArgs()
        {
        }
        public static new TaskTemplateRequiredFieldInfoArgs Empty => new TaskTemplateRequiredFieldInfoArgs();
    }
}
