// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iottwinmaker

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type ComponentTypeStatusErrorPropertiesCode string

const (
	ComponentTypeStatusErrorPropertiesCodeValidationError = ComponentTypeStatusErrorPropertiesCode("VALIDATION_ERROR")
	ComponentTypeStatusErrorPropertiesCodeInternalFailure = ComponentTypeStatusErrorPropertiesCode("INTERNAL_FAILURE")
)

type ComponentTypeStatusState string

const (
	ComponentTypeStatusStateCreating = ComponentTypeStatusState("CREATING")
	ComponentTypeStatusStateUpdating = ComponentTypeStatusState("UPDATING")
	ComponentTypeStatusStateDeleting = ComponentTypeStatusState("DELETING")
	ComponentTypeStatusStateActive   = ComponentTypeStatusState("ACTIVE")
	ComponentTypeStatusStateError    = ComponentTypeStatusState("ERROR")
)

type ComponentTypeStatusStateOutput struct{ *pulumi.OutputState }

func (ComponentTypeStatusStateOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ComponentTypeStatusState)(nil)).Elem()
}

func (o ComponentTypeStatusStateOutput) ToComponentTypeStatusStateOutput() ComponentTypeStatusStateOutput {
	return o
}

func (o ComponentTypeStatusStateOutput) ToComponentTypeStatusStateOutputWithContext(ctx context.Context) ComponentTypeStatusStateOutput {
	return o
}

func (o ComponentTypeStatusStateOutput) ToComponentTypeStatusStatePtrOutput() ComponentTypeStatusStatePtrOutput {
	return o.ToComponentTypeStatusStatePtrOutputWithContext(context.Background())
}

func (o ComponentTypeStatusStateOutput) ToComponentTypeStatusStatePtrOutputWithContext(ctx context.Context) ComponentTypeStatusStatePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v ComponentTypeStatusState) *ComponentTypeStatusState {
		return &v
	}).(ComponentTypeStatusStatePtrOutput)
}

func (o ComponentTypeStatusStateOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o ComponentTypeStatusStateOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e ComponentTypeStatusState) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o ComponentTypeStatusStateOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o ComponentTypeStatusStateOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e ComponentTypeStatusState) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type ComponentTypeStatusStatePtrOutput struct{ *pulumi.OutputState }

func (ComponentTypeStatusStatePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ComponentTypeStatusState)(nil)).Elem()
}

func (o ComponentTypeStatusStatePtrOutput) ToComponentTypeStatusStatePtrOutput() ComponentTypeStatusStatePtrOutput {
	return o
}

func (o ComponentTypeStatusStatePtrOutput) ToComponentTypeStatusStatePtrOutputWithContext(ctx context.Context) ComponentTypeStatusStatePtrOutput {
	return o
}

func (o ComponentTypeStatusStatePtrOutput) Elem() ComponentTypeStatusStateOutput {
	return o.ApplyT(func(v *ComponentTypeStatusState) ComponentTypeStatusState {
		if v != nil {
			return *v
		}
		var ret ComponentTypeStatusState
		return ret
	}).(ComponentTypeStatusStateOutput)
}

func (o ComponentTypeStatusStatePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o ComponentTypeStatusStatePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *ComponentTypeStatusState) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type EntityStatusErrorPropertiesCode string

const (
	EntityStatusErrorPropertiesCodeValidationError = EntityStatusErrorPropertiesCode("VALIDATION_ERROR")
	EntityStatusErrorPropertiesCodeInternalFailure = EntityStatusErrorPropertiesCode("INTERNAL_FAILURE")
)

type EntityStatusState string

const (
	EntityStatusStateCreating = EntityStatusState("CREATING")
	EntityStatusStateUpdating = EntityStatusState("UPDATING")
	EntityStatusStateDeleting = EntityStatusState("DELETING")
	EntityStatusStateActive   = EntityStatusState("ACTIVE")
	EntityStatusStateError    = EntityStatusState("ERROR")
)

type EntityStatusStateOutput struct{ *pulumi.OutputState }

func (EntityStatusStateOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*EntityStatusState)(nil)).Elem()
}

func (o EntityStatusStateOutput) ToEntityStatusStateOutput() EntityStatusStateOutput {
	return o
}

func (o EntityStatusStateOutput) ToEntityStatusStateOutputWithContext(ctx context.Context) EntityStatusStateOutput {
	return o
}

func (o EntityStatusStateOutput) ToEntityStatusStatePtrOutput() EntityStatusStatePtrOutput {
	return o.ToEntityStatusStatePtrOutputWithContext(context.Background())
}

func (o EntityStatusStateOutput) ToEntityStatusStatePtrOutputWithContext(ctx context.Context) EntityStatusStatePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v EntityStatusState) *EntityStatusState {
		return &v
	}).(EntityStatusStatePtrOutput)
}

func (o EntityStatusStateOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o EntityStatusStateOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e EntityStatusState) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o EntityStatusStateOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o EntityStatusStateOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e EntityStatusState) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type EntityStatusStatePtrOutput struct{ *pulumi.OutputState }

func (EntityStatusStatePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**EntityStatusState)(nil)).Elem()
}

func (o EntityStatusStatePtrOutput) ToEntityStatusStatePtrOutput() EntityStatusStatePtrOutput {
	return o
}

func (o EntityStatusStatePtrOutput) ToEntityStatusStatePtrOutputWithContext(ctx context.Context) EntityStatusStatePtrOutput {
	return o
}

func (o EntityStatusStatePtrOutput) Elem() EntityStatusStateOutput {
	return o.ApplyT(func(v *EntityStatusState) EntityStatusState {
		if v != nil {
			return *v
		}
		var ret EntityStatusState
		return ret
	}).(EntityStatusStateOutput)
}

func (o EntityStatusStatePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o EntityStatusStatePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *EntityStatusState) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(ComponentTypeStatusStateOutput{})
	pulumi.RegisterOutputType(ComponentTypeStatusStatePtrOutput{})
	pulumi.RegisterOutputType(EntityStatusStateOutput{})
	pulumi.RegisterOutputType(EntityStatusStatePtrOutput{})
}
