// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Backup
{
    public static class GetFramework
    {
        /// <summary>
        /// Contains detailed information about a framework. Frameworks contain controls, which evaluate and report on your backup events and resources. Frameworks generate daily compliance results.
        /// </summary>
        public static Task<GetFrameworkResult> InvokeAsync(GetFrameworkArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetFrameworkResult>("aws-native:backup:getFramework", args ?? new GetFrameworkArgs(), options.WithDefaults());

        /// <summary>
        /// Contains detailed information about a framework. Frameworks contain controls, which evaluate and report on your backup events and resources. Frameworks generate daily compliance results.
        /// </summary>
        public static Output<GetFrameworkResult> Invoke(GetFrameworkInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetFrameworkResult>("aws-native:backup:getFramework", args ?? new GetFrameworkInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetFrameworkArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// An Amazon Resource Name (ARN) that uniquely identifies Framework as a resource
        /// </summary>
        [Input("frameworkArn", required: true)]
        public string FrameworkArn { get; set; } = null!;

        public GetFrameworkArgs()
        {
        }
        public static new GetFrameworkArgs Empty => new GetFrameworkArgs();
    }

    public sealed class GetFrameworkInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// An Amazon Resource Name (ARN) that uniquely identifies Framework as a resource
        /// </summary>
        [Input("frameworkArn", required: true)]
        public Input<string> FrameworkArn { get; set; } = null!;

        public GetFrameworkInvokeArgs()
        {
        }
        public static new GetFrameworkInvokeArgs Empty => new GetFrameworkInvokeArgs();
    }


    [OutputType]
    public sealed class GetFrameworkResult
    {
        /// <summary>
        /// The date and time that a framework is created, in ISO 8601 representation. The value of CreationTime is accurate to milliseconds. For example, 2020-07-10T15:00:00.000-08:00 represents the 10th of July 2020 at 3:00 PM 8 hours behind UTC.
        /// </summary>
        public readonly string? CreationTime;
        /// <summary>
        /// The deployment status of a framework. The statuses are: `CREATE_IN_PROGRESS | UPDATE_IN_PROGRESS | DELETE_IN_PROGRESS | COMPLETED | FAILED`
        /// </summary>
        public readonly string? DeploymentStatus;
        /// <summary>
        /// An Amazon Resource Name (ARN) that uniquely identifies Framework as a resource
        /// </summary>
        public readonly string? FrameworkArn;
        /// <summary>
        /// Contains detailed information about all of the controls of a framework. Each framework must contain at least one control.
        /// </summary>
        public readonly ImmutableArray<Outputs.FrameworkControl> FrameworkControls;
        /// <summary>
        /// An optional description of the framework with a maximum 1,024 characters.
        /// </summary>
        public readonly string? FrameworkDescription;
        /// <summary>
        /// A framework consists of one or more controls. Each control governs a resource, such as backup plans, backup selections, backup vaults, or recovery points. You can also turn AWS Config recording on or off for each resource. The statuses are:
        /// 
        /// `ACTIVE` when recording is turned on for all resources governed by the framework.
        /// 
        /// `PARTIALLY_ACTIVE` when recording is turned off for at least one resource governed by the framework.
        /// 
        /// `INACTIVE` when recording is turned off for all resources governed by the framework.
        /// 
        /// `UNAVAILABLE` when AWS Backup is unable to validate recording status at this time.
        /// </summary>
        public readonly string? FrameworkStatus;
        /// <summary>
        /// Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.
        /// </summary>
        public readonly ImmutableArray<Outputs.FrameworkTag> FrameworkTags;

        [OutputConstructor]
        private GetFrameworkResult(
            string? creationTime,

            string? deploymentStatus,

            string? frameworkArn,

            ImmutableArray<Outputs.FrameworkControl> frameworkControls,

            string? frameworkDescription,

            string? frameworkStatus,

            ImmutableArray<Outputs.FrameworkTag> frameworkTags)
        {
            CreationTime = creationTime;
            DeploymentStatus = deploymentStatus;
            FrameworkArn = frameworkArn;
            FrameworkControls = frameworkControls;
            FrameworkDescription = frameworkDescription;
            FrameworkStatus = frameworkStatus;
            FrameworkTags = frameworkTags;
        }
    }
}
