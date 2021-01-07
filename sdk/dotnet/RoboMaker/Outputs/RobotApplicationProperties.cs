// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.RoboMaker.Outputs
{

    [OutputType]
    public sealed class RobotApplicationProperties
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplication.html#cfn-robomaker-robotapplication-currentrevisionid
        /// </summary>
        public readonly string? CurrentRevisionId;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplication.html#cfn-robomaker-robotapplication-name
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplication.html#cfn-robomaker-robotapplication-robotsoftwaresuite
        /// </summary>
        public readonly Outputs.RobotApplicationRobotSoftwareSuite RobotSoftwareSuite;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplication.html#cfn-robomaker-robotapplication-sources
        /// </summary>
        public readonly ImmutableArray<Outputs.RobotApplicationSourceConfig> Sources;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplication.html#cfn-robomaker-robotapplication-tags
        /// </summary>
        public readonly Union<System.Text.Json.JsonElement, string>? Tags;

        [OutputConstructor]
        private RobotApplicationProperties(
            string? CurrentRevisionId,

            string? Name,

            Outputs.RobotApplicationRobotSoftwareSuite RobotSoftwareSuite,

            ImmutableArray<Outputs.RobotApplicationSourceConfig> Sources,

            Union<System.Text.Json.JsonElement, string>? Tags)
        {
            this.CurrentRevisionId = CurrentRevisionId;
            this.Name = Name;
            this.RobotSoftwareSuite = RobotSoftwareSuite;
            this.Sources = Sources;
            this.Tags = Tags;
        }
    }
}