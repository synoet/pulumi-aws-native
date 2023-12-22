// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Inputs
{

    /// <summary>
    /// Default storage settings for a space.
    /// </summary>
    public sealed class UserProfileDefaultSpaceStorageSettingsArgs : global::Pulumi.ResourceArgs
    {
        [Input("defaultEbsStorageSettings")]
        public Input<Inputs.UserProfileDefaultEbsStorageSettingsArgs>? DefaultEbsStorageSettings { get; set; }

        public UserProfileDefaultSpaceStorageSettingsArgs()
        {
        }
        public static new UserProfileDefaultSpaceStorageSettingsArgs Empty => new UserProfileDefaultSpaceStorageSettingsArgs();
    }
}
