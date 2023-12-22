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
    /// The JupyterLab app settings.
    /// </summary>
    public sealed class UserProfileJupyterLabAppSettingsArgs : global::Pulumi.ResourceArgs
    {
        [Input("codeRepositories")]
        private InputList<Inputs.UserProfileCodeRepositoryArgs>? _codeRepositories;

        /// <summary>
        /// A list of CodeRepositories available for use with JupyterLab apps.
        /// </summary>
        public InputList<Inputs.UserProfileCodeRepositoryArgs> CodeRepositories
        {
            get => _codeRepositories ?? (_codeRepositories = new InputList<Inputs.UserProfileCodeRepositoryArgs>());
            set => _codeRepositories = value;
        }

        [Input("customImages")]
        private InputList<Inputs.UserProfileCustomImageArgs>? _customImages;

        /// <summary>
        /// A list of custom images available for use for JupyterLab apps
        /// </summary>
        public InputList<Inputs.UserProfileCustomImageArgs> CustomImages
        {
            get => _customImages ?? (_customImages = new InputList<Inputs.UserProfileCustomImageArgs>());
            set => _customImages = value;
        }

        /// <summary>
        /// The default instance type and the Amazon Resource Name (ARN) of the default SageMaker image used by the JupyterLab app.
        /// </summary>
        [Input("defaultResourceSpec")]
        public Input<Inputs.UserProfileResourceSpecArgs>? DefaultResourceSpec { get; set; }

        [Input("lifecycleConfigArns")]
        private InputList<string>? _lifecycleConfigArns;

        /// <summary>
        /// A list of LifecycleConfigArns available for use with JupyterLab apps.
        /// </summary>
        public InputList<string> LifecycleConfigArns
        {
            get => _lifecycleConfigArns ?? (_lifecycleConfigArns = new InputList<string>());
            set => _lifecycleConfigArns = value;
        }

        public UserProfileJupyterLabAppSettingsArgs()
        {
        }
        public static new UserProfileJupyterLabAppSettingsArgs Empty => new UserProfileJupyterLabAppSettingsArgs();
    }
}
